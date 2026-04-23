from typing import List, Tuple
from sklearn.feature_extraction.text import TfidfVectorizer
import re


class KeywordExtractor:
    def __init__(self):
        self.vectorizer = TfidfVectorizer(
            stop_words='english',
            max_features=10,
            ngram_range=(1, 2),
            token_pattern=r'(?u)\b[a-zA-Z][a-zA-Z]+\b'
        )
        self.stop_words = {
            'the', 'a', 'an', 'is', 'are', 'was', 'were', 'be', 'been', 'being',
            'have', 'has', 'had', 'do', 'does', 'did', 'will', 'would', 'could',
            'should', 'may', 'might', 'must', 'shall', 'can', 'need', 'dare',
            'to', 'of', 'in', 'for', 'on', 'with', 'at', 'by', 'from', 'as',
            'into', 'through', 'during', 'before', 'after', 'above', 'below',
            'and', 'but', 'or', 'nor', 'so', 'yet', 'both', 'either', 'neither',
            'not', 'only', 'own', 'same', 'than', 'too', 'very', 'just', 'also',
            'it', 'its', 'this', 'that', 'these', 'those', 'what', 'which',
            'who', 'whom', 'whose', 'where', 'when', 'why', 'how', 'i', 'you',
            'he', 'she', 'we', 'they', 'me', 'him', 'her', 'us', 'them', 'my',
            'your', 'his', 'our', 'their', 'mine', 'yours', 'hers', 'ours', 'theirs'
        }

    def extract_keywords(self, text: str) -> List[str]:
        words = re.findall(r'\b[a-zA-Z][a-zA-Z]+\b', text.lower())
        filtered = [w for w in words if w not in self.stop_words and len(w) > 2]
        unique_keywords = list(dict.fromkeys(filtered))
        return unique_keywords[:5]

    def highlight_keywords(self, fact: str, query: str) -> Tuple[str, List[str]]:
        fact_keywords = self.extract_keywords(fact)
        query_keywords = self.extract_keywords(query)
        
        matched = [kw for kw in fact_keywords if kw in query_keywords]
        
        highlighted = fact
        for kw in matched:
            pattern = re.compile(re.escape(kw), re.IGNORECASE)
            highlighted = pattern.sub(f'**{kw}**', highlighted)
        
        return highlighted, matched