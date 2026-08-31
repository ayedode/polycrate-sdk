from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.effective_criticality_enum import EffectiveCriticalityEnum, check_effective_criticality_enum
from ..models.last_state_enum import LastStateEnum, check_last_state_enum
from ..models.project_kind_enum import ProjectKindEnum, check_project_kind_enum
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.organization_simple import OrganizationSimple
    from ..models.project_list_active_condition_instances_item import ProjectListActiveConditionInstancesItem
    from ..models.project_list_created import ProjectListCreated


T = TypeVar("T", bound="ProjectList")


@_attrs_define
class ProjectList:
    """Lightweight serializer for Project list views.

    Attributes:
        id (UUID):
        name (str): Gibt die bevorzugte UI-Anzeige (display_name) zurück.
        state (LastStateEnum): * `OK` - Ok
            * `WARNING` - Warning
            * `CRITICAL` - Critical
            * `READY` - Ready
            * `DEGRADED` - Degraded
            * `DOWN` - Down
        labels (Any):
        condition_instance_count (int): Number of active ConditionInstances linked to this object (Spec 419).
            Uses prefetched data (_prefetched_active_conditions) when available to avoid N+1.
        active_condition_instances (list[ProjectListActiveConditionInstancesItem]):
        organization (OrganizationSimple): Simple Organization serializer for nested representations.

            Includes `url` field for direct navigation.
        organization_priority (bool): True when the object's organization has priority=True.
        created (ProjectListCreated):
        archived (bool): Archived objects are not shown in the UI and are not managed by the API.
        effective_criticality (EffectiveCriticalityEnum | None):
        url (str): Gibt die absolute URL zum Object zurück.
        kind_display (str):
        computed_cost (None | str):
        kind (ProjectKindEnum | Unset): * `onboarding` - Onboarding
            * `offboarding` - Offboarding
            * `ongoing` - Ongoing
        active (bool | Unset): Whether this project is currently active
        start_date (datetime.date | None | Unset): Project start date
        end_date (datetime.date | None | Unset): Project end date
    """

    id: UUID
    name: str
    state: LastStateEnum
    labels: Any
    condition_instance_count: int
    active_condition_instances: list[ProjectListActiveConditionInstancesItem]
    organization: OrganizationSimple
    organization_priority: bool
    created: ProjectListCreated
    archived: bool
    effective_criticality: EffectiveCriticalityEnum | None
    url: str
    kind_display: str
    computed_cost: None | str
    kind: ProjectKindEnum | Unset = UNSET
    active: bool | Unset = UNSET
    start_date: datetime.date | None | Unset = UNSET
    end_date: datetime.date | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = str(self.id)

        name = self.name

        state: str = self.state

        labels = self.labels

        condition_instance_count = self.condition_instance_count

        active_condition_instances = []
        for active_condition_instances_item_data in self.active_condition_instances:
            active_condition_instances_item = active_condition_instances_item_data.to_dict()
            active_condition_instances.append(active_condition_instances_item)

        organization = self.organization.to_dict()

        organization_priority = self.organization_priority

        created = self.created.to_dict()

        archived = self.archived

        effective_criticality: None | str
        if isinstance(self.effective_criticality, str):
            effective_criticality = self.effective_criticality
        else:
            effective_criticality = self.effective_criticality

        url = self.url

        kind_display = self.kind_display

        computed_cost: None | str
        computed_cost = self.computed_cost

        kind: str | Unset = UNSET
        if not isinstance(self.kind, Unset):
            kind = self.kind

        active = self.active

        start_date: None | str | Unset
        if isinstance(self.start_date, Unset):
            start_date = UNSET
        elif isinstance(self.start_date, datetime.date):
            start_date = self.start_date.isoformat()
        else:
            start_date = self.start_date

        end_date: None | str | Unset
        if isinstance(self.end_date, Unset):
            end_date = UNSET
        elif isinstance(self.end_date, datetime.date):
            end_date = self.end_date.isoformat()
        else:
            end_date = self.end_date

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "name": name,
                "state": state,
                "labels": labels,
                "condition_instance_count": condition_instance_count,
                "active_condition_instances": active_condition_instances,
                "organization": organization,
                "organization_priority": organization_priority,
                "created": created,
                "archived": archived,
                "effective_criticality": effective_criticality,
                "url": url,
                "kind_display": kind_display,
                "computed_cost": computed_cost,
            }
        )
        if kind is not UNSET:
            field_dict["kind"] = kind
        if active is not UNSET:
            field_dict["active"] = active
        if start_date is not UNSET:
            field_dict["start_date"] = start_date
        if end_date is not UNSET:
            field_dict["end_date"] = end_date

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.organization_simple import OrganizationSimple
        from ..models.project_list_active_condition_instances_item import ProjectListActiveConditionInstancesItem
        from ..models.project_list_created import ProjectListCreated

        d = dict(src_dict)
        id = UUID(d.pop("id"))

        name = d.pop("name")

        state = check_last_state_enum(d.pop("state"))

        labels = d.pop("labels")

        condition_instance_count = d.pop("condition_instance_count")

        active_condition_instances = []
        _active_condition_instances = d.pop("active_condition_instances")
        for active_condition_instances_item_data in _active_condition_instances:
            active_condition_instances_item = ProjectListActiveConditionInstancesItem.from_dict(
                active_condition_instances_item_data
            )

            active_condition_instances.append(active_condition_instances_item)

        organization = OrganizationSimple.from_dict(d.pop("organization"))

        organization_priority = d.pop("organization_priority")

        created = ProjectListCreated.from_dict(d.pop("created"))

        archived = d.pop("archived")

        def _parse_effective_criticality(data: object) -> EffectiveCriticalityEnum | None:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                effective_criticality_type_0 = check_effective_criticality_enum(data)

                return effective_criticality_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(EffectiveCriticalityEnum | None, data)

        effective_criticality = _parse_effective_criticality(d.pop("effective_criticality"))

        url = d.pop("url")

        kind_display = d.pop("kind_display")

        def _parse_computed_cost(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        computed_cost = _parse_computed_cost(d.pop("computed_cost"))

        _kind = d.pop("kind", UNSET)
        kind: ProjectKindEnum | Unset
        if isinstance(_kind, Unset):
            kind = UNSET
        else:
            kind = check_project_kind_enum(_kind)

        active = d.pop("active", UNSET)

        def _parse_start_date(data: object) -> datetime.date | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                start_date_type_0 = datetime.date.fromisoformat(data)

                return start_date_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.date | None | Unset, data)

        start_date = _parse_start_date(d.pop("start_date", UNSET))

        def _parse_end_date(data: object) -> datetime.date | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                end_date_type_0 = datetime.date.fromisoformat(data)

                return end_date_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.date | None | Unset, data)

        end_date = _parse_end_date(d.pop("end_date", UNSET))

        project_list = cls(
            id=id,
            name=name,
            state=state,
            labels=labels,
            condition_instance_count=condition_instance_count,
            active_condition_instances=active_condition_instances,
            organization=organization,
            organization_priority=organization_priority,
            created=created,
            archived=archived,
            effective_criticality=effective_criticality,
            url=url,
            kind_display=kind_display,
            computed_cost=computed_cost,
            kind=kind,
            active=active,
            start_date=start_date,
            end_date=end_date,
        )

        project_list.additional_properties = d
        return project_list

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
