from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.k8s_cluster_kind_enum import K8SClusterKindEnum, check_k8s_cluster_kind_enum

if TYPE_CHECKING:
    from ..models.organization_simple import OrganizationSimple
    from ..models.workspace_simple import WorkspaceSimple


T = TypeVar("T", bound="K8SClusterSimple")


@_attrs_define
class K8SClusterSimple:
    """
    Attributes:
        id (UUID):
        name (str):
        reconciliation_running (bool):
        kind (K8SClusterKindEnum): * `polycrate` - Polycrate
            * `generic` - Generic
            * `loopback` - Loopback
        installed (bool):
        is_host_cluster (bool):
        is_infrastructure_cluster (bool):
        kubernetes_version (None | str):
        kubeconfig_ca_cert_expiry_date (datetime.datetime | None):
        kubeconfig_client_cert_expiry_date (datetime.datetime | None):
        api_server_cert_expiry_date (datetime.datetime | None):
        organization (OrganizationSimple): Simple Organization serializer for nested representations.

            Includes `url` field for direct navigation.
        workspace (WorkspaceSimple):
        credential (None | UUID):
    """

    id: UUID
    name: str
    reconciliation_running: bool
    kind: K8SClusterKindEnum
    installed: bool
    is_host_cluster: bool
    is_infrastructure_cluster: bool
    kubernetes_version: None | str
    kubeconfig_ca_cert_expiry_date: datetime.datetime | None
    kubeconfig_client_cert_expiry_date: datetime.datetime | None
    api_server_cert_expiry_date: datetime.datetime | None
    organization: OrganizationSimple
    workspace: WorkspaceSimple
    credential: None | UUID
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = str(self.id)

        name = self.name

        reconciliation_running = self.reconciliation_running

        kind: str = self.kind

        installed = self.installed

        is_host_cluster = self.is_host_cluster

        is_infrastructure_cluster = self.is_infrastructure_cluster

        kubernetes_version: None | str
        kubernetes_version = self.kubernetes_version

        kubeconfig_ca_cert_expiry_date: None | str
        if isinstance(self.kubeconfig_ca_cert_expiry_date, datetime.datetime):
            kubeconfig_ca_cert_expiry_date = self.kubeconfig_ca_cert_expiry_date.isoformat()
        else:
            kubeconfig_ca_cert_expiry_date = self.kubeconfig_ca_cert_expiry_date

        kubeconfig_client_cert_expiry_date: None | str
        if isinstance(self.kubeconfig_client_cert_expiry_date, datetime.datetime):
            kubeconfig_client_cert_expiry_date = self.kubeconfig_client_cert_expiry_date.isoformat()
        else:
            kubeconfig_client_cert_expiry_date = self.kubeconfig_client_cert_expiry_date

        api_server_cert_expiry_date: None | str
        if isinstance(self.api_server_cert_expiry_date, datetime.datetime):
            api_server_cert_expiry_date = self.api_server_cert_expiry_date.isoformat()
        else:
            api_server_cert_expiry_date = self.api_server_cert_expiry_date

        organization = self.organization.to_dict()

        workspace = self.workspace.to_dict()

        credential: None | str
        if isinstance(self.credential, UUID):
            credential = str(self.credential)
        else:
            credential = self.credential

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "name": name,
                "reconciliation_running": reconciliation_running,
                "kind": kind,
                "installed": installed,
                "is_host_cluster": is_host_cluster,
                "is_infrastructure_cluster": is_infrastructure_cluster,
                "kubernetes_version": kubernetes_version,
                "kubeconfig_ca_cert_expiry_date": kubeconfig_ca_cert_expiry_date,
                "kubeconfig_client_cert_expiry_date": kubeconfig_client_cert_expiry_date,
                "api_server_cert_expiry_date": api_server_cert_expiry_date,
                "organization": organization,
                "workspace": workspace,
                "credential": credential,
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

        reconciliation_running = d.pop("reconciliation_running")

        kind = check_k8s_cluster_kind_enum(d.pop("kind"))

        installed = d.pop("installed")

        is_host_cluster = d.pop("is_host_cluster")

        is_infrastructure_cluster = d.pop("is_infrastructure_cluster")

        def _parse_kubernetes_version(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        kubernetes_version = _parse_kubernetes_version(d.pop("kubernetes_version"))

        def _parse_kubeconfig_ca_cert_expiry_date(data: object) -> datetime.datetime | None:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                kubeconfig_ca_cert_expiry_date_type_0 = datetime.datetime.fromisoformat(data)

                return kubeconfig_ca_cert_expiry_date_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None, data)

        kubeconfig_ca_cert_expiry_date = _parse_kubeconfig_ca_cert_expiry_date(d.pop("kubeconfig_ca_cert_expiry_date"))

        def _parse_kubeconfig_client_cert_expiry_date(data: object) -> datetime.datetime | None:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                kubeconfig_client_cert_expiry_date_type_0 = datetime.datetime.fromisoformat(data)

                return kubeconfig_client_cert_expiry_date_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None, data)

        kubeconfig_client_cert_expiry_date = _parse_kubeconfig_client_cert_expiry_date(
            d.pop("kubeconfig_client_cert_expiry_date")
        )

        def _parse_api_server_cert_expiry_date(data: object) -> datetime.datetime | None:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                api_server_cert_expiry_date_type_0 = datetime.datetime.fromisoformat(data)

                return api_server_cert_expiry_date_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None, data)

        api_server_cert_expiry_date = _parse_api_server_cert_expiry_date(d.pop("api_server_cert_expiry_date"))

        organization = OrganizationSimple.from_dict(d.pop("organization"))

        workspace = WorkspaceSimple.from_dict(d.pop("workspace"))

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

        k8s_cluster_simple = cls(
            id=id,
            name=name,
            reconciliation_running=reconciliation_running,
            kind=kind,
            installed=installed,
            is_host_cluster=is_host_cluster,
            is_infrastructure_cluster=is_infrastructure_cluster,
            kubernetes_version=kubernetes_version,
            kubeconfig_ca_cert_expiry_date=kubeconfig_ca_cert_expiry_date,
            kubeconfig_client_cert_expiry_date=kubeconfig_client_cert_expiry_date,
            api_server_cert_expiry_date=api_server_cert_expiry_date,
            organization=organization,
            workspace=workspace,
            credential=credential,
        )

        k8s_cluster_simple.additional_properties = d
        return k8s_cluster_simple

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
