from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.credential_kind_enum import CredentialKindEnum, check_credential_kind_enum
from ..models.provider_enum import ProviderEnum, check_provider_enum

T = TypeVar("T", bound="CredentialSimple")


@_attrs_define
class CredentialSimple:
    """Simple serializer for embedding Credential in other serializers.

    Attributes:
        id (UUID):
        name (str):
        reconciliation_running (bool):
        kind (CredentialKindEnum): * `api-key` - API Key
            * `kubeconfig` - Kubeconfig
            * `s3-credential` - S3 Credential
            * `ssh-keys` - SSH Keys
            * `generic` - Generic
            * `webhook` - Webhook
            * `agent_token` - Agent Token
            * `workspace-encryption` - Workspace Encryption
            * `oci-registry-credential` - OCI Registry Credential
            * `helm-repository-credential` - Helm Repository Credential
            * `apmstack-metrics-credential` - APM Stack Metrics Credential
            * `unified-apm-credential` - Unified APM Credential
            * `unified-registry-credential` - Unified Registry Credential
            * `apmstack-logs-credential` - APM Stack Logs Credential
            * `apmstack-traces-credential` - APM Stack Traces Credential
            * `domain-auth-code` - Domain Auth Code
            * `dns-provider` - DNS Provider
            * `system_api_key` - System API Key
            * `org_api_key` - Org API Key
            * `controlplane-token` - Controlplane Token
            * `provider-account` - Provider Account
        provider (ProviderEnum): * `loopback` - Loopback
            * `hetzner_cloud` - HETZNER Cloud
            * `hetzner_robot` - HETZNER Robot
            * `bare_metal` - Bare-Metal
            * `powerdns` - PowerDNS
            * `cloudflare` - Cloudflare
            * `rook-ceph` - Rook Ceph
            * `polycrate` - Polycrate
            * `kubernetes` - Kubernetes
            * `helm` - Helm
            * `generic` - Generic
            * `victorialogs` - VictoriaLogs
            * `system` - System
        url (str):
    """

    id: UUID
    name: str
    reconciliation_running: bool
    kind: CredentialKindEnum
    provider: ProviderEnum
    url: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = str(self.id)

        name = self.name

        reconciliation_running = self.reconciliation_running

        kind: str = self.kind

        provider: str = self.provider

        url = self.url

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "name": name,
                "reconciliation_running": reconciliation_running,
                "kind": kind,
                "provider": provider,
                "url": url,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = UUID(d.pop("id"))

        name = d.pop("name")

        reconciliation_running = d.pop("reconciliation_running")

        kind = check_credential_kind_enum(d.pop("kind"))

        provider = check_provider_enum(d.pop("provider"))

        url = d.pop("url")

        credential_simple = cls(
            id=id,
            name=name,
            reconciliation_running=reconciliation_running,
            kind=kind,
            provider=provider,
            url=url,
        )

        credential_simple.additional_properties = d
        return credential_simple

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
