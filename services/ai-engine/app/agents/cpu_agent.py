def analyze_cpu(cpu_value: float, pod_id: str):
    
    if cpu_value < 0.2:
        return [{
            "type": "cpu",
            "pod": pod_id,
            "level": "LOW",
            "message": "CPU usage is normal"
        }]
    
    elif cpu_value < 0.7:
        return [{
            "type": "cpu",
            "pod": pod_id,
            "level": "MEDIUM",
            "message": "Moderate CPU usage"
        }]
    
    else:
        return [{
            "type": "cpu",
            "pod": pod_id,
            "level": "HIGH",
            "message": "High CPU usage detected"
        }]