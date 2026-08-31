from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.slo_object_type_enum import SloObjectTypeEnum, check_slo_object_type_enum
from ..models.slo_status_enum import SloStatusEnum, check_slo_status_enum

if TYPE_CHECKING:
    from ..models.slo_downtime_ref import SloDowntimeRef
    from ..models.slo_organization_ref import SloOrganizationRef
    from ..models.slo_workspace_ref import SloWorkspaceRef


T = TypeVar("T", bound="SloObject")


@_attrs_define
class SloObject:
    """
    Attributes:
        id (UUID):
        name (str):
        type_ (SloObjectTypeEnum): * `Endpoint` - Endpoint
            * `K8sCluster` - K8sCluster
        organization (SloOrganizationRef):
        workspace (SloWorkspaceRef):
        slo_availability (float): Current SLO availability percentage
        slo_status (SloStatusEnum): * `ok` - ok
            * `at_risk` - at_risk
            * `breach` - breach
        state (str): Current object state (up, down, degraded)
        active_downtime (None | SloDowntimeRef):
        url (str): Object detail URL
    """

    id: UUID
    name: str
    type_: SloObjectTypeEnum
    organization: SloOrganizationRef
    workspace: SloWorkspaceRef
    slo_availability: float
    slo_status: SloStatusEnum
    state: str
    active_downtime: None | SloDowntimeRef
    url: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.slo_downtime_ref import SloDowntimeRef

        id = str(self.id)

        name = self.name

        type_: str = self.type_

        organization = self.organization.to_dict()

        workspace = self.workspace.to_dict()

        slo_availability = self.slo_availability

        slo_status: str = self.slo_status

        state = self.state

        active_downtime: dict[str, Any] | None
        if isinstance(self.active_downtime, SloDowntimeRef):
            active_downtime = self.active_downtime.to_dict()
        else:
            active_downtime = self.active_downtime

        url = self.url

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "name": name,
                "type": type_,
                "organization": organization,
                "workspace": workspace,
                "slo_availability": slo_availability,
                "slo_status": slo_status,
                "state": state,
                "active_downtime": active_downtime,
                "url": url,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.slo_downtime_ref import SloDowntimeRef
        from ..models.slo_organization_ref import SloOrganizationRef
        from ..models.slo_workspace_ref import SloWorkspaceRef

        d = dict(src_dict)
        id = UUID(d.pop("id"))

        name = d.pop("name")

        type_ = check_slo_object_type_enum(d.pop("type"))

        organization = SloOrganizationRef.from_dict(d.pop("organization"))

        workspace = SloWorkspaceRef.from_dict(d.pop("workspace"))

        slo_availability = d.pop("slo_availability")

        slo_status = check_slo_status_enum(d.pop("slo_status"))

        state = d.pop("state")

        def _parse_active_downtime(data: object) -> None | SloDowntimeRef:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                active_downtime_type_1 = SloDowntimeRef.from_dict(data)

                return active_downtime_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | SloDowntimeRef, data)

        active_downtime = _parse_active_downtime(d.pop("active_downtime"))

        url = d.pop("url")

        slo_object = cls(
            id=id,
            name=name,
            type_=type_,
            organization=organization,
            workspace=workspace,
            slo_availability=slo_availability,
            slo_status=slo_status,
            state=state,
            active_downtime=active_downtime,
            url=url,
        )

        slo_object.additional_properties = d
        return slo_object

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
