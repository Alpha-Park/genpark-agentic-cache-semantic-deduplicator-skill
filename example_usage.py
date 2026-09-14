import sys
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

from client import AgenticCacheSemanticDeduplicatorClient

def main():
    client = AgenticCacheSemanticDeduplicatorClient()
    # First query -> Miss & insert
    r1 = client.lookup_or_insert_cache("Compare battery life of Roborock S8 vs Dreame X40")
    print(f"Query 1: {r1['cache_status']} (Key: {r1.get('inserted_key')})")

    # Second near-identical query -> Hit
    r2 = client.lookup_or_insert_cache("Compare the battery life of Roborock S8 and Dreame X40")
    print(f"Query 2: {r2['cache_status']} (Matched: {r2.get('matched_key')} | Similarity: {r2.get('jaccard_similarity')})")
    print(f"Tokens Saved: {r2.get('tokens_saved')} | Cost Saved: ${r2.get('cost_saved_usd')}")

if __name__ == '__main__':
    main()
