from prometheus_client import Gauge, CollectorRegistry, push_to_gateway  # noqa


def main():
    instance = 'localhost:9090'
    name = 'gauge_demo'
    documentation = 'gauge demo docs'
    push_url = 'localhost:9091'
    registry = CollectorRegistry()
    g = Gauge(
        name=name,
        documentation=documentation,
        registry=registry,
        labelnames=('instance', 'metric')
    )
    res = g.labels(instance=instance, metric=name).set(9898)
    print(f"Res: {res}")
    res = push_to_gateway(push_url, job=name, registry=registry)
    print(f"Res: {res}")


if __name__ == "__main__":
    main()

