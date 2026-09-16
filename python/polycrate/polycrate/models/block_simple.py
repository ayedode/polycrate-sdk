from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.block_kind_enum import BlockKindEnum, check_block_kind_enum

if TYPE_CHECKING:
    from ..models.organization_simple import OrganizationSimple
    from ..models.workspace_simple import WorkspaceSimple


T = TypeVar("T", bound="BlockSimple")


@_attrs_define
class BlockSimple:
    """
    Attributes:
        id (UUID):
        name (str):
        reconciliation_running (bool):
        kind (BlockKindEnum): * `dockerapp` - Docker App
            * `linuxapp` - Linux App
            * `k8sapp` - Kubernetes App
            * `k8sappinstance` - Kubernetes App Instance
            * `k8scluster` - Kubernetes Cluster
            * `library` - Block Library
            * `generic` - Anything
        type_ (None | str):
        flavor (None | str):
        workspace (WorkspaceSimple):
        organization (OrganizationSimple): Simple Organization serializer for nested representations.

            Includes `url` field for direct navigation.
        url (str):
    """

    id: UUID
    name: str
    reconciliation_running: bool
    kind: BlockKindEnum
    type_: None | str
    flavor: None | str
    workspace: WorkspaceSimple
    organization: OrganizationSimple
    url: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = str(self.id)

        name = self.name

        reconciliation_running = self.reconciliation_running

        kind: str = self.kind

        type_: None | str
        type_ = self.type_

        flavor: None | str
        flavor = self.flavor

        workspace = self.workspace.to_dict()

        organization = self.organization.to_dict()

        url = self.url

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "name": name,
                "reconciliation_running": reconciliation_running,
                "kind": kind,
                "type": type_,
                "flavor": flavor,
                "workspace": workspace,
                "organization": organization,
                "url": url,
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

        kind = check_block_kind_enum(d.pop("kind"))

        def _parse_type_(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        type_ = _parse_type_(d.pop("type"))

        def _parse_flavor(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        flavor = _parse_flavor(d.pop("flavor"))

        workspace = WorkspaceSimple.from_dict(d.pop("workspace"))

        organization = OrganizationSimple.from_dict(d.pop("organization"))

        url = d.pop("url")

        block_simple = cls(
            id=id,
            name=name,
            reconciliation_running=reconciliation_running,
            kind=kind,
            type_=type_,
            flavor=flavor,
            workspace=workspace,
            organization=organization,
            url=url,
        )

        block_simple.additional_properties = d
        return block_simple

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
