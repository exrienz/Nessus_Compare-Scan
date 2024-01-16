import json

def parse_file(filename):
    findings = []
    with open(filename, 'r') as file:
        for line in file:
            severity, issue, ip_addresses = line.strip().split(';')
            ip_list = ip_addresses.split(',')
            finding = {'severity': severity.strip(), 'issue': issue.strip(), 'ip_addresses': ip_list}
            findings.append(finding)
    return findings

def convert_to_json(old_filename, new_filename):
    old_findings = parse_file(old_filename)
    new_findings = parse_file(new_filename)

    old_json_filename = 'old.json'
    new_json_filename = 'new.json'

    with open(old_json_filename, 'w') as old_json_file:
        json.dump(old_findings, old_json_file, indent=2)

    with open(new_json_filename, 'w') as new_json_file:
        json.dump(new_findings, new_json_file, indent=2)

    return old_findings, new_findings

def compare_and_sort(old_findings, new_findings):
    findings_result = []

    for new_finding in new_findings:
        matching_old_findings = [old_finding for old_finding in old_findings if old_finding['issue'] == new_finding['issue']]
        if not matching_old_findings:
            findings_result.append({'status': 'new', **new_finding})

    for old_finding in old_findings:
        matching_new_findings = [new_finding for new_finding in new_findings if new_finding['issue'] == old_finding['issue']]
        if not matching_new_findings:
            findings_result.append({'status': 'close', **old_finding})
        else:
            findings_result.append({'status': 'open', **matching_new_findings[0]})

    sorted_findings = sorted(findings_result, key=lambda x: ('Critical', 'High', 'Medium', 'Low').index(x['severity']))

    return sorted_findings

if __name__ == "__main__":
    old_filename = 'old.txt'
    new_filename = 'new.txt'

    old_findings, new_findings = convert_to_json(old_filename, new_filename)

    for finding in compare_and_sort(old_findings, new_findings):
        print(f"{finding['status'].capitalize()}, {finding['severity'].capitalize()}, {finding['issue']}, {' '.join(finding['ip_addresses'])}")
