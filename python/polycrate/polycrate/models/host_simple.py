from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.host_simple_bootstrap_status import HostSimpleBootstrapStatus, check_host_simple_bootstrap_status
from ..models.host_simple_kind import HostSimpleKind, check_host_simple_kind
from ..models.host_simple_provider import HostSimpleProvider, check_host_simple_provider
from ..models.host_simple_role import HostSimpleRole, check_host_simple_role

if TYPE_CHECKING:
    from ..models.organization_simple import OrganizationSimple
    from ..models.workspace_simple import WorkspaceSimple


T = TypeVar("T", bound="HostSimple")


@_attrs_define
class HostSimple:
    """
    Attributes:
        id (UUID):
        name (str):
        url (str):
        reconciliation_running (bool):
        kind (HostSimpleKind): * `vm` - Virtual Machine
            * `bare_metal` - Bare-Metal Machine
        provider (HostSimpleProvider): * `loopback` - Loopback
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
        workspace (WorkspaceSimple):
        organization (OrganizationSimple): Simple Organization serializer for nested representations.

            Includes `url` field for direct navigation.
        hostname (str):
        credential (None | UUID):
        role (HostSimpleRole): Host role (e.g. k8s-worker). Spec: polycrate spec inspect 729.

            * `k8s-worker` - Kubernetes Worker
            * `k8s-controlplane` - Kubernetes Controlplane
            * `generic` - Generic
        bootstrap_status (HostSimpleBootstrapStatus): IaaS/machine bootstrap lifecycle. Spec: polycrate spec inspect
            729.

            * `pending` - Pending
            * `provisioning` - Provisioning
            * `ready` - Ready
            * `joining` - Joining
            * `failed` - Failed
            * `deprovisioning` - Deprovisioning
    """

    id: UUID
    name: str
    url: str
    reconciliation_running: bool
    kind: HostSimpleKind
    provider: HostSimpleProvider
    workspace: WorkspaceSimple
    organization: OrganizationSimple
    hostname: str
    credential: None | UUID
    role: HostSimpleRole
    bootstrap_status: HostSimpleBootstrapStatus
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = str(self.id)

        name = self.name

        url = self.url

        reconciliation_running = self.reconciliation_running

        kind: str = self.kind

        provider: str = self.provider

        workspace = self.workspace.to_dict()

        organization = self.organization.to_dict()

        hostname = self.hostname

        credential: None | str
        if isinstance(self.credential, UUID):
            credential = str(self.credential)
        else:
            credential = self.credential

        role: str = self.role

        bootstrap_status: str = self.bootstrap_status

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "name": name,
                "url": url,
                "reconciliation_running": reconciliation_running,
                "kind": kind,
                "provider": provider,
                "workspace": workspace,
                "organization": organization,
                "hostname": hostname,
                "credential": credential,
                "role": role,
                "bootstrap_status": bootstrap_status,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.organization_simple import OrganizationSimple  # noqa: PLC0415
        from ..models.workspace_simple import WorkspaceSimple  # noqa: PLC0415

        d = dict(src_dict)
        id = UUID(d.pop("id"))

        name = d.pop("name")

        url = d.pop("url")

        reconciliation_running = d.pop("reconciliation_running")

        kind = check_host_simple_kind(d.pop("kind"))

        provider = check_host_simple_provider(d.pop("provider"))

        workspace = WorkspaceSimple.from_dict(d.pop("workspace"))

        organization = OrganizationSimple.from_dict(d.pop("organization"))

        hostname = d.pop("hostname")

        def _parse_credential(data: object) -> None | UUID:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                credential_type_0 = UUID(data)

                return credential_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | UUID, data)

        credential = _parse_credential(d.pop("credential"))

        role = check_host_simple_role(d.pop("role"))

        bootstrap_status = check_host_simple_bootstrap_status(d.pop("bootstrap_status"))

        host_simple = cls(
            id=id,
            name=name,
            url=url,
            reconciliation_running=reconciliation_running,
            kind=kind,
            provider=provider,
            workspace=workspace,
            organization=organization,
            hostname=hostname,
            credential=credential,
            role=role,
            bootstrap_status=bootstrap_status,
        )

        host_simple.additional_properties = d
        return host_simple

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
