import wmi

def get_running_services():
    c = wmi.WMI()
    services = []

    # Query running services
    for service in c.Win32_Service(State="Running"):
        services.append(service.Caption)

    return services

# Get the list of running services
running_services = get_running_services()

# Save the list to a text file
with open('running_services.txt', 'w') as file:
    for service in running_services:
        file.write(service + '\n')

print("List of running services saved to running_services.txt")
