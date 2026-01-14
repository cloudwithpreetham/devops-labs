import psutil


def get_threshold(metric_name):
    """
    Takes threshold input from the user.
    Example: CPU threshold = 80
    """
    while True:
        try:
            value = float(input(f"Enter {metric_name} threshold percentage: "))
            if 0 <= value <= 100:
                return value
            else:
                print("Please enter a value between 0 and 100.")
        except ValueError:
            print("Invalid input. Please enter a number.")


def get_system_metrics():
    """
    Fetches current CPU, memory, and disk usage.
    """
    metrics = {
        "CPU": psutil.cpu_percent(interval=1),
        "Memory": psutil.virtual_memory().percent,
        "Disk": psutil.disk_usage("/").percent,
    }

    return metrics


def check_health(metrics, thresholds):
    """
    Compares system metrics with threshold values.
    """
    print("\n========== System Health Report ==========\n")

    for metric_name, usage in metrics.items():
        threshold = thresholds[metric_name]

        print(f"{metric_name} Usage: {usage}%")
        print(f"{metric_name} Threshold: {threshold}%")

        if usage > threshold:
            print(f"Status: WARNING - {metric_name} usage is above threshold\n")
        else:
            print(f"Status: OK - {metric_name} usage is normal\n")


def main():
    print("DevOps System Health Checker")
    print("--------------------------------")

    thresholds = {
        "CPU": get_threshold("CPU"),
        "Memory": get_threshold("Memory"),
        "Disk": get_threshold("Disk"),
    }

    metrics = get_system_metrics()

    check_health(metrics, thresholds)


if __name__ == "__main__":
    main()
