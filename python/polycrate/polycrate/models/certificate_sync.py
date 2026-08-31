from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="CertificateSync")


@_attrs_define
class CertificateSync:
    """Serializer for syncing certificates from Polycrate Operator.

    Attributes:
        cert_data (Any): Raw cert-manager Certificate CR data
        k8s_cluster_id (int): K8sCluster ID
        organization_id (int): Organization ID
        workspace_id (int | None | Unset): Optional Workspace ID
    """

    cert_data: Any
    k8s_cluster_id: int
    organization_id: int
    workspace_id: int | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        cert_data = self.cert_data

        k8s_cluster_id = self.k8s_cluster_id

        organization_id = self.organization_id

        workspace_id: int | None | Unset
        if isinstance(self.workspace_id, Unset):
            workspace_id = UNSET
        else:
            workspace_id = self.workspace_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "cert_data": cert_data,
                "k8s_cluster_id": k8s_cluster_id,
                "organization_id": organization_id,
            }
        )
        if workspace_id is not UNSET:
            field_dict["workspace_id"] = workspace_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        cert_data = d.pop("cert_data")

        k8s_cluster_id = d.pop("k8s_cluster_id")

        organization_id = d.pop("organization_id")

        def _parse_workspace_id(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        workspace_id = _parse_workspace_id(d.pop("workspace_id", UNSET))

        certificate_sync = cls(
            cert_data=cert_data,
            k8s_cluster_id=k8s_cluster_id,
            organization_id=organization_id,
            workspace_id=workspace_id,
        )

        certificate_sync.additional_properties = d
        return certificate_sync

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
