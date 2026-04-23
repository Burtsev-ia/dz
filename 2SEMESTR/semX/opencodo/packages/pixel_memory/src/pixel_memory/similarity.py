from typing import List, Tuple
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer

USE_SENTENCE_TRANSFORMERS = False

try:
    from sentence_transformers import SentenceTransformer
    USE_SENTENCE_TRANSFORMERS = True
except ImportError:
    pass


class SimilarityEngine:
    def __init__(self, model_name: str = "all-MiniLM-L6-v2"):
        self.use_st = USE_SENTENCE_TRANSFORMERS
        self.vectorizer = TfidfVectorizer(
            stop_words='english',
            ngram_range=(1, 2),
            max_features=5000
        )
        self.is_fitted = False
        
        if self.use_st:
            try:
                self.model = SentenceTransformer(model_name)
            except Exception:
                self.use_st = False

    def encode_facts(self, facts: List[str]) -> np.ndarray:
        if self.use_st:
            try:
                return self.model.encode(facts, convert_to_numpy=True)
            except Exception:
                self.use_st = False
        
        if not facts:
            return np.array([]).reshape(0, 1)
        
        self.is_fitted = True
        return self.vectorizer.fit_transform(facts).toarray()

    def encode_query(self, query: str) -> np.ndarray:
        if self.use_st:
            try:
                return self.model.encode([query], convert_to_numpy=True)[0]
            except Exception:
                self.use_st = False
        
        if not self.is_fitted:
            return np.array([])
        
        return self.vectorizer.transform([query]).toarray()[0]

    def compute_similarity(self, query_embedding: np.ndarray, fact_embedding: np.ndarray) -> float:
        if query_embedding.shape != fact_embedding.shape:
            min_len = min(query_embedding.shape[0], fact_embedding.shape[0])
            q = query_embedding[:min_len]
            f = fact_embedding[:min_len]
        else:
            q = query_embedding
            f = fact_embedding
        
        q_norm = q / (np.linalg.norm(q) + 1e-8)
        f_norm = f / (np.linalg.norm(f) + 1e-8)
        return float(np.dot(q_norm, f_norm))

    def find_best_match(self, query: str, facts: List[str], threshold: float = 0.0) -> Tuple[int, float]:
        if not facts:
            return -1, -1.0
        
        embeddings = self.encode_facts(facts)
        query_embedding = self.encode_query(query)
        
        best_score = -1.0
        best_idx = -1
        
        for idx, fact_emb in enumerate(embeddings):
            score = self.compute_similarity(query_embedding, fact_emb)
            if score > best_score and score >= threshold:
                best_score = score
                best_idx = idx
        
        return best_idx, best_score

    def is_similar(self, text1: str, text2: str, threshold: float = 0.6) -> bool:
        if text1 == text2:
            return True
        
        if self.use_st:
            try:
                emb1 = self.model.encode([text1])[0]
                emb2 = self.model.encode([text2])[0]
                similarity = float(np.dot(emb1, emb2) / (np.linalg.norm(emb1) * np.linalg.norm(emb2) + 1e-8))
                return similarity >= threshold
            except Exception:
                pass
        
        try:
            self.vectorizer.fit([text1, text2])
            emb1 = self.vectorizer.transform([text1]).toarray()[0]
            emb2 = self.vectorizer.transform([text2]).toarray()[0]
            emb1_norm = emb1 / (np.linalg.norm(emb1) + 1e-8)
            emb2_norm = emb2 / (np.linalg.norm(emb2) + 1e-8)
            similarity = float(np.dot(emb1_norm, emb2_norm))
            return similarity >= threshold
        except Exception:
            return False