from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.slo_object import SloObject
    from ..models.slo_organization_filter import SloOrganizationFilter
    from ..models.slo_stats import SloStats
    from ..models.slo_workspace_filter import SloWorkspaceFilter


T = TypeVar("T", bound="SloOverviewResponse")


@_attrs_define
class SloOverviewResponse:
    """
    Attributes:
        stats (SloStats):
        objects (list[SloObject]): List of objects with issues (breach, at_risk, or in downtime)
        organizations (list[SloOrganizationFilter]): Available organizations for filtering
        workspaces (list[SloWorkspaceFilter]): Available workspaces for filtering (filtered by organization if set)
    """

    stats: SloStats
    objects: list[SloObject]
    organizations: list[SloOrganizationFilter]
    workspaces: list[SloWorkspaceFilter]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        stats = self.stats.to_dict()

        objects = []
        for objects_item_data in self.objects:
            objects_item = objects_item_data.to_dict()
            objects.append(objects_item)

        organizations = []
        for organizations_item_data in self.organizations:
            organizations_item = organizations_item_data.to_dict()
            organizations.append(organizations_item)

        workspaces = []
        for workspaces_item_data in self.workspaces:
            workspaces_item = workspaces_item_data.to_dict()
            workspaces.append(workspaces_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "stats": stats,
                "objects": objects,
                "organizations": organizations,
                "workspaces": workspaces,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.slo_object import SloObject
        from ..models.slo_organization_filter import SloOrganizationFilter
        from ..models.slo_stats import SloStats
        from ..models.slo_workspace_filter import SloWorkspaceFilter

        d = dict(src_dict)
        stats = SloStats.from_dict(d.pop("stats"))

        objects = []
        _objects = d.pop("objects")
        for objects_item_data in _objects:
            objects_item = SloObject.from_dict(objects_item_data)

            objects.append(objects_item)

        organizations = []
        _organizations = d.pop("organizations")
        for organizations_item_data in _organizations:
            organizations_item = SloOrganizationFilter.from_dict(organizations_item_data)

            organizations.append(organizations_item)

        workspaces = []
        _workspaces = d.pop("workspaces")
        for workspaces_item_data in _workspaces:
            workspaces_item = SloWorkspaceFilter.from_dict(workspaces_item_data)

            workspaces.append(workspaces_item)

        slo_overview_response = cls(
            stats=stats,
            objects=objects,
            organizations=organizations,
            workspaces=workspaces,
        )

        slo_overview_response.additional_properties = d
        return slo_overview_response

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
