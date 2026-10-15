from typing import Literal

ComplianceReportProvider = Literal[
    "bare_metal",
    "cloudflare",
    "generic",
    "helm",
    "hetzner_cloud",
    "hetzner_robot",
    "kubernetes",
    "loopback",
    "polycrate",
    "powerdns",
    "rook-ceph",
    "system",
    "victorialogs",
]

COMPLIANCE_REPORT_PROVIDER_VALUES: set[ComplianceReportProvider] = {
    "bare_metal",
    "cloudflare",
    "generic",
    "helm",
    "hetzner_cloud",
    "hetzner_robot",
    "kubernetes",
    "loopback",
    "polycrate",
    "powerdns",
    "rook-ceph",
    "system",
    "victorialogs",
}


def check_compliance_report_provider(value: str) -> ComplianceReportProvider:
    if value in COMPLIANCE_REPORT_PROVIDER_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {COMPLIANCE_REPORT_PROVIDER_VALUES!r}")
