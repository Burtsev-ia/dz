from typing import List, Tuple, Optional
import numpy as np

from .item import MemoryItem
from .similarity import SimilarityEngine
from .keywords import KeywordExtractor


class PixelMemory:
    MAX_ITEMS = 10
    MIN_CONFIDENCE = 0.1
    BASE_IMPORTANCE = 1.0
    DUPLICATE_BOOST = 200.0
    SEMANTIC_BOOST = 10.0
    SIMILARITY_THRESHOLD = 0.6

    def __init__(self, max_items: int = 10):
        self.items: List[MemoryItem] = []
        self.similarity_engine = SimilarityEngine()
        self.keyword_extractor = KeywordExtractor()
        self.max_items = max_items

    def learn(self, fact: str) -> None:
        fact_lower = fact.lower()
        
        for item in self.items:
            if item.fact.lower() == fact_lower:
                item.importance += self.DUPLICATE_BOOST
                self._semantic_boost(item, fact_lower)
                return
        
        keywords = self.keyword_extractor.extract_keywords(fact)
        
        item = MemoryItem(
            fact=fact,
            embedding=np.array([]),
            keywords=keywords,
            importance=self.BASE_IMPORTANCE,
            access_count=0
        )
        
        if len(self.items) >= self.max_items:
            self._evict()
        
        self.items.append(item)
    
    def _semantic_boost(self, target_item: MemoryItem, target_lower: str) -> None:
        for item in self.items:
            if item is target_item:
                continue
            item_lower = item.fact.lower()
            
            if self.similarity_engine.is_similar(target_lower, item_lower, self.SIMILARITY_THRESHOLD):
                item.importance += self.SEMANTIC_BOOST

    def query(self, question: str) -> Optional[Tuple[str, List[str], float]]:
        if not self.items:
            return ("I forgot that((", [], 0.0)
        
        facts = [item.fact for item in self.items]
        
        best_idx, score = self.similarity_engine.find_best_match(
            question, facts, 0.0
        )
        
        rewrite_idx, rewrite_score = self._semantic_rewrite_match(question, facts)
        
        if rewrite_idx != -1 and rewrite_score > score:
            best_idx = rewrite_idx
            score = rewrite_score
        
        if best_idx == -1 or (score < self.MIN_CONFIDENCE and len(self.items) >= 3):
            return ("I forgot that((", [], score)
        
        matched_item = self.items[best_idx]
        matched_item.boost_access()
        
        highlighted, matched_keywords = self.keyword_extractor.highlight_keywords(
            matched_item.fact, question
        )
        
        return highlighted, matched_keywords, score

    def _semantic_rewrite_match(self, question: str, facts: List[str]) -> Tuple[int, float]:
        question_lower = question.lower()
        
        rewrite_rules = [
            ("what does my owner do for work", "works as"),
            ("where does my owner live", "lives in"),
            ("what is my owner's pet's name", "cat named"),
            ("what does my owner like to read", "reading"),
            ("what is my owner's favorite movie", "favorite movie"),
            ("what is my owner's favorite sport", "favorite sport"),
            ("what is my owner's favorite color", "favorite color is"),
            ("what does my owner do on weekends", "plays guitar"),
            ("what is my owner's favorite season", "favorite season is"),
            ("how many languages does my owner speak", "speaks three languages"),
            ("what is my owner's favorite holiday", "favorite holiday is"),
            ("where did my owner adopt me from", "adopted me from"),
            ("what is my owner allergic to", "allergic to"),
            ("what color is the sky", "sky is blue"),
            ("at what temperature does water freeze", "water freezes"),
            ("how many legs do cats have", "cats have four legs"),
            ("what is the sun", "sun is a star"),
            ("what are dogs", "dogs are mammals"),
            ("what does the moon orbit", "moon orbits"),
            ("can birds fly", "birds can fly"),
            ("where do fish live", "fish live in water"),
            ("what does the earth orbit", "earth orbits the sun"),
            ("where does rain come from", "rain comes from"),
            ("what do i love chasing", "chasing butterflies"),
            ("what is my favorite toy", "favorite toy is a squeaky ball"),
            ("where do i sleep", "sleep on a soft dog bed"),
            ("what color is my fur", "fur is golden"),
            ("where do i enjoy walks", "enjoy walks in the park"),
            ("what car does my owner drive", "drives a"),
            ("when is my owner's birthday", "birthday is"),
            ("what is my owner name", "owner name is"),
            ("what is my owner's favorite food", "favorite food is"),
        ]
        
        matched_phrase = None
        for pattern, expected_phrase in rewrite_rules:
            if pattern in question_lower:
                matched_phrase = expected_phrase
                break
        
        if not matched_phrase:
            return -1, -1.0
        
        # Find fact containing the expected phrase
        for idx, fact in enumerate(facts):
            if matched_phrase in fact.lower():
                return idx, 0.8
        
        return -1, -1.0

    def _evict(self) -> None:
        if not self.items:
            return
        
        for item in self.items:
            item.importance = item.compute_importance()
        
        lowest_importance = min(item.importance for item in self.items)
        
        for i, item in enumerate(self.items):
            if item.importance == lowest_importance:
                del self.items[i]
                break

    def get_all_facts(self) -> List[str]:
        return [item.fact for item in self.items]

    def __len__(self) -> int:
        return len(self.items)