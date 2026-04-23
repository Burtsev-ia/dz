from pixel_memory import PixelMemory, Evaluator


class TestPixelMemory:
    def test_initialization(self):
        memory = PixelMemory(max_items=10)
        assert len(memory) == 0
        assert memory.max_items == 10

    def test_learn_single_fact(self):
        memory = PixelMemory(max_items=10)
        memory.learn("My owner's name is Sarah")
        assert len(memory) == 1

    def test_learn_multiple_facts(self):
        memory = PixelMemory(max_items=10)
        facts = ["Fact 1", "Fact 2", "Fact 3"]
        for f in facts:
            memory.learn(f)
        assert len(memory) == 3

    def test_max_capacity_eviction(self):
        memory = PixelMemory(max_items=3)
        memory.learn("Fact 1")
        memory.learn("Fact 2")
        memory.learn("Fact 3")
        assert len(memory) == 3
        
        memory.learn("Fact 4")
        assert len(memory) == 3
        
        facts = memory.get_all_facts()
        assert "Fact 1" not in facts

    def test_query_returns_result(self):
        memory = PixelMemory(max_items=10)
        memory.learn("My owner lives in New York City")
        result = memory.query("Where does my owner live?")
        assert result is not None
        fact, keywords, score = result
        assert "New York City" in fact

    def test_query_empty_memory(self):
        memory = PixelMemory(max_items=10)
        result = memory.query("Some question")
        assert result is not None
        assert result[0] == "I forgot that(("

    def test_query_boosts_access_count(self):
        memory = PixelMemory(max_items=10)
        memory.learn("My owner is Sarah")
        
        result1 = memory.query("What's my owner's name?")
        assert result1 is not None
        
        state = memory.get_all_facts()
        assert any("Sarah" in i for i in state)

    def test_important_facts_survive_eviction(self):
        memory = PixelMemory(max_items=3)
        
        memory.learn("My owner's name is Sarah")
        memory.learn("The sky is blue")
        memory.learn("Water is wet")
        
        for _ in range(3):
            memory.query("What is my owner's name?")
        
        memory.learn("New fact 1")
        memory.learn("New fact 2")
        memory.learn("New fact 3")
        
        facts = memory.get_all_facts()
        assert any("Sarah" in f for f in facts)


class TestEvaluator:
    def test_run_benchmark_empty_sequence(self):
        memory = PixelMemory(max_items=10)
        evaluator = Evaluator(memory)
        results, query_results = evaluator.run_benchmark([])
        assert results == {}
        assert query_results == []

    def test_run_benchmark_fact_only(self):
        memory = PixelMemory(max_items=10)
        evaluator = Evaluator(memory)
        sequence = [("fact", "A fact")]
        results, query_results = evaluator.run_benchmark(sequence)
        assert query_results == []

    def test_run_benchmark_query_only(self):
        memory = PixelMemory(max_items=10)
        evaluator = Evaluator(memory)
        sequence = [("query", ("Question?", "Answer"))]
        results, query_results = evaluator.run_benchmark(sequence)
        assert query_results == [False]

    def test_mixed_sequence(self):
        memory = PixelMemory(max_items=10)
        evaluator = Evaluator(memory)
        
        sequence = [
            ("fact", "My owner is Sarah"),
            ("query", ("What's my owner?", "My owner is Sarah")),
        ]
        
        results, query_results = evaluator.run_benchmark(sequence)
        assert len(query_results) == 1
        assert query_results[0]


class TestKeywordExtraction:
    def test_extract_keywords(self):
        from pixel_memory.keywords import KeywordExtractor
        extractor = KeywordExtractor()
        keywords = extractor.extract_keywords("My owner's favorite color is purple")
        assert "owner" in keywords or "favorite" in keywords or "color" in keywords

    def test_highlight_keywords(self):
        from pixel_memory.keywords import KeywordExtractor
        extractor = KeywordExtractor()
        highlighted, matched = extractor.highlight_keywords(
            "My owner's favorite color is purple",
            "What is my owner's favorite color?"
        )
        assert "**" in highlighted or len(matched) > 0