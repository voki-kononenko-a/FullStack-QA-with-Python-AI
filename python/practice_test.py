def validate_endpoints_sla(endpoints_data: dict, max_sla_seconds: float = 1.5):
    """Проход по словарю и распаковка пар (ключ + значение). В строке цикла мы создаём сразу две переменные через запятую."""
    for endpoint_name, response_time in endpoints_data.items():
        assert response_time <= max_sla_seconds, (
            f"Эндпоинт '{endpoint_name}' отвечает слишком медленно: {response_time}s "
            f"(Лимит SLA: {max_sla_seconds}s)"
        )


services_metrics = {
    "/api/v1/auth": 0.45,
    "/api/v1/catalog": 1.20,
    "/api/v1/checkout": 1.5,
    "/api/v1/health": 0.10
}

validate_endpoints_sla(services_metrics)
