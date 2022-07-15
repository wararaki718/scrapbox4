from dataclasses import asdict

from opensearchpy import OpenSearch

from config import ClientConfig, SearchConfig


def main():
    client_config = ClientConfig()
    client = OpenSearch(**asdict(client_config))

    search_config = SearchConfig()
    response = client.indices.create(search_config.index_name, body=search_config.index_body)
    print(f"create index: {response}")

    document = {
        "title": "sample",
        "director": "test",
        "year": "2000"
    }
    response = client.index(
        index = search_config.index_name,
        body = document,
        id = "1",
        refresh = True
    )
    print(f"add document: {response}")

    query = {
        "size": 5,
        "query": {
            "multi_match": {
                "query": "miller",
                "fields": ["title^2", "director"]
            }
        }
    }
    response = client.search(
        body = query,
        index = search_config.index_name
    )
    print(f"search: {response}")

    response = client.delete(
        index = search_config.index_name,
        id = "1"
    )
    print(f"delete document: {response}")

    response = client.indices.delete(index=search_config.index_name)
    print(f"delete index: {response}")

    print("DONE")


if __name__ == "__main__":
    main()
