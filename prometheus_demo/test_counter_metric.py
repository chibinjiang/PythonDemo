from prometheus_client import Counter, CollectorRegistry, push_to_gateway  # noqa


def main():
    instance = 'localhost:9090'
    name = 'counter_demo'
    documentation = 'counter demo docs'
    push_url = 'localhost:9091'
    registry = CollectorRegistry()
    counter = Counter(
        name=name, 
        documentation=documentation, 
        registry=registry,
        labelnames=('instance', 'metric')
    )
    res = counter.labels(instance=instance, metric=name).inc(amount=9999)
    print(f"Res: {res}")
    res = push_to_gateway(push_url, job=name, registry=registry)
    print(f"Res: {res}")


if __name__ == "__main__":
    main()

