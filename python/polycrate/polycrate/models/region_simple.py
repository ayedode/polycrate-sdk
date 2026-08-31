from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.workspace_simple import WorkspaceSimple


T = TypeVar("T", bound="RegionSimple")


@_attrs_define
class RegionSimple:
    """
    Attributes:
        id (UUID):
        name (str):
        display_name (None | str): The display name is used to display the object in the UI. It can be different from
            the name.
        platform_features (list[str]): Active platform services: 's3', 'loadbalancer', 'apm', 'dns', 'controlplane'
        platform_service (bool): If True: managed by system owner org, available platform-wide to all organizations.
        workspace (WorkspaceSimple):
        url (str):
    """

    id: UUID
    name: str
    display_name: None | str
    platform_features: list[str]
    platform_service: bool
    workspace: WorkspaceSimple
    url: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = str(self.id)

        name = self.name

        display_name: None | str
        display_name = self.display_name

        platform_features = self.platform_features

        platform_service = self.platform_service

        workspace = self.workspace.to_dict()

        url = self.url

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "name": name,
                "display_name": display_name,
                "platform_features": platform_features,
                "platform_service": platform_service,
                "workspace": workspace,
                "url": url,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.workspace_simple import WorkspaceSimple

        d = dict(src_dict)
        id = UUID(d.pop("id"))

        name = d.pop("name")

        def _parse_display_name(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        display_name = _parse_display_name(d.pop("display_name"))

        platform_features = cast(list[str], d.pop("platform_features"))

        platform_service = d.pop("platform_service")

        workspace = WorkspaceSimple.from_dict(d.pop("workspace"))

        url = d.pop("url")

        region_simple = cls(
            id=id,
            name=name,
            display_name=display_name,
            platform_features=platform_features,
            platform_service=platform_service,
            workspace=workspace,
            url=url,
        )

        region_simple.additional_properties = d
        return region_simple

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
