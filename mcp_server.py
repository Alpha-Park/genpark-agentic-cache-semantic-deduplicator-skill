import json, sys
from client import AgenticCacheSemanticDeduplicatorClient

def handle_mcp_request(payload):
    method = payload.get("method")
    req_id = payload.get("id", 1)
    if method == "initialize":
        return {"jsonrpc": "2.0", "id": req_id, "result": {"protocolVersion": "2024-11-05", "serverInfo": {"name": "cache-semantic-deduplicator", "version": "1.0.0"}}}
    elif method == "tools/list":
        return {"jsonrpc": "2.0", "id": req_id, "result": {"tools": [{"name": "lookup_or_insert_cache", "description": "Look up prompt in semantic cache via Jaccard similarity or insert new entry."}]}}
    elif method == "tools/call":
        client = AgenticCacheSemanticDeduplicatorClient()
        res = client.lookup_or_insert_cache()
        return {"jsonrpc": "2.0", "id": req_id, "result": {"content": [{"type": "text", "text": json.dumps(res, indent=2)}]}}
    return {"jsonrpc": "2.0", "id": req_id, "result": {"status": "ACTIVE"}}

if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "--test":
        print(json.dumps(handle_mcp_request({"method": "tools/list"})))
    else:
        client = AgenticCacheSemanticDeduplicatorClient()
        print(json.dumps(client.lookup_or_insert_cache(), indent=2))
