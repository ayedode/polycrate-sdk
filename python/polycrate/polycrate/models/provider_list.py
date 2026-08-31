from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.effective_criticality_enum import EffectiveCriticalityEnum, check_effective_criticality_enum
from ..models.last_state_enum import LastStateEnum, check_last_state_enum
from ..models.pop_provider_kind_enum import PopProviderKindEnum, check_pop_provider_kind_enum
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.provider_list_active_condition_instances_item import ProviderListActiveConditionInstancesItem
    from ..models.provider_list_created import ProviderListCreated


T = TypeVar("T", bound="ProviderList")


@_attrs_define
class ProviderList:
    """List serializer for Provider V2 tables.

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
        conditions (Any): Conditions are managed by the API and will be added during the reconcile phase. Some
            conditions are `degrading`, meaning an object becomes DEGRADED if it has such a condition.
        condition_instance_count (int): Number of active ConditionInstances linked to this object (Spec 419).
            Uses prefetched data (_prefetched_active_conditions) when available to avoid N+1.
        active_condition_instances (list[ProviderListActiveConditionInstancesItem]):
        organization (None | str):
        organization_priority (bool): True when the object's organization has priority=True.
        workspace (None | str):
        created (ProviderListCreated):
        archived (bool): Archived objects are not shown in the UI and are not managed by the API.
        reconciliation_running (bool):
        effective_criticality (EffectiveCriticalityEnum | None):
        url (str): Gibt die absolute URL zum Object zurück.
        has_icon (bool):
        icon_url (None | str):
        is_class_icon (bool):
        pop_count (int):
        datasource_count (int):
        kind (PopProviderKindEnum | Unset): * `infrastructure` - Infrastructure
            * `hardware` - Hardware
            * `software` - Software
        legal_name (None | str | Unset): Legal company name (e.g. 'Hetzner Online GmbH')
        slug (None | str | Unset): URL-friendly identifier (auto-generated from name if empty)
        active (bool | Unset): When false, hidden from new PoP/DataSource/workspace PoP assignments.
        asn (Any | Unset): List of AS Numbers, e.g. [{"name": "Default", "value": "AS24940"}]
        certifications (Any | Unset): List of certifications held by this provider (e.g. ISO27001, TISAX, SOC2)
    """

    id: UUID
    name: str
    state: LastStateEnum
    labels: Any
    conditions: Any
    condition_instance_count: int
    active_condition_instances: list[ProviderListActiveConditionInstancesItem]
    organization: None | str
    organization_priority: bool
    workspace: None | str
    created: ProviderListCreated
    archived: bool
    reconciliation_running: bool
    effective_criticality: EffectiveCriticalityEnum | None
    url: str
    has_icon: bool
    icon_url: None | str
    is_class_icon: bool
    pop_count: int
    datasource_count: int
    kind: PopProviderKindEnum | Unset = UNSET
    legal_name: None | str | Unset = UNSET
    slug: None | str | Unset = UNSET
    active: bool | Unset = UNSET
    asn: Any | Unset = UNSET
    certifications: Any | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = str(self.id)

        name = self.name

        state: str = self.state

        labels = self.labels

        conditions = self.conditions

        condition_instance_count = self.condition_instance_count

        active_condition_instances = []
        for active_condition_instances_item_data in self.active_condition_instances:
            active_condition_instances_item = active_condition_instances_item_data.to_dict()
            active_condition_instances.append(active_condition_instances_item)

        organization: None | str
        organization = self.organization

        organization_priority = self.organization_priority

        workspace: None | str
        workspace = self.workspace

        created = self.created.to_dict()

        archived = self.archived

        reconciliation_running = self.reconciliation_running

        effective_criticality: None | str
        if isinstance(self.effective_criticality, str):
            effective_criticality = self.effective_criticality
        else:
            effective_criticality = self.effective_criticality

        url = self.url

        has_icon = self.has_icon

        icon_url: None | str
        icon_url = self.icon_url

        is_class_icon = self.is_class_icon

        pop_count = self.pop_count

        datasource_count = self.datasource_count

        kind: str | Unset = UNSET
        if not isinstance(self.kind, Unset):
            kind = self.kind

        legal_name: None | str | Unset
        if isinstance(self.legal_name, Unset):
            legal_name = UNSET
        else:
            legal_name = self.legal_name

        slug: None | str | Unset
        if isinstance(self.slug, Unset):
            slug = UNSET
        else:
            slug = self.slug

        active = self.active

        asn = self.asn

        certifications = self.certifications

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "name": name,
                "state": state,
                "labels": labels,
                "conditions": conditions,
                "condition_instance_count": condition_instance_count,
                "active_condition_instances": active_condition_instances,
                "organization": organization,
                "organization_priority": organization_priority,
                "workspace": workspace,
                "created": created,
                "archived": archived,
                "reconciliation_running": reconciliation_running,
                "effective_criticality": effective_criticality,
                "url": url,
                "has_icon": has_icon,
                "icon_url": icon_url,
                "is_class_icon": is_class_icon,
                "pop_count": pop_count,
                "datasource_count": datasource_count,
            }
        )
        if kind is not UNSET:
            field_dict["kind"] = kind
        if legal_name is not UNSET:
            field_dict["legal_name"] = legal_name
        if slug is not UNSET:
            field_dict["slug"] = slug
        if active is not UNSET:
            field_dict["active"] = active
        if asn is not UNSET:
            field_dict["asn"] = asn
        if certifications is not UNSET:
            field_dict["certifications"] = certifications

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.provider_list_active_condition_instances_item import ProviderListActiveConditionInstancesItem
        from ..models.provider_list_created import ProviderListCreated

        d = dict(src_dict)
        id = UUID(d.pop("id"))

        name = d.pop("name")

        state = check_last_state_enum(d.pop("state"))

        labels = d.pop("labels")

        conditions = d.pop("conditions")

        condition_instance_count = d.pop("condition_instance_count")

        active_condition_instances = []
        _active_condition_instances = d.pop("active_condition_instances")
        for active_condition_instances_item_data in _active_condition_instances:
            active_condition_instances_item = ProviderListActiveConditionInstancesItem.from_dict(
                active_condition_instances_item_data
            )

            active_condition_instances.append(active_condition_instances_item)

        def _parse_organization(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        organization = _parse_organization(d.pop("organization"))

        organization_priority = d.pop("organization_priority")

        def _parse_workspace(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        workspace = _parse_workspace(d.pop("workspace"))

        created = ProviderListCreated.from_dict(d.pop("created"))

        archived = d.pop("archived")

        reconciliation_running = d.pop("reconciliation_running")

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

        has_icon = d.pop("has_icon")

        def _parse_icon_url(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        icon_url = _parse_icon_url(d.pop("icon_url"))

        is_class_icon = d.pop("is_class_icon")

        pop_count = d.pop("pop_count")

        datasource_count = d.pop("datasource_count")

        _kind = d.pop("kind", UNSET)
        kind: PopProviderKindEnum | Unset
        if isinstance(_kind, Unset):
            kind = UNSET
        else:
            kind = check_pop_provider_kind_enum(_kind)

        def _parse_legal_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        legal_name = _parse_legal_name(d.pop("legal_name", UNSET))

        def _parse_slug(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        slug = _parse_slug(d.pop("slug", UNSET))

        active = d.pop("active", UNSET)

        asn = d.pop("asn", UNSET)

        certifications = d.pop("certifications", UNSET)

        provider_list = cls(
            id=id,
            name=name,
            state=state,
            labels=labels,
            conditions=conditions,
            condition_instance_count=condition_instance_count,
            active_condition_instances=active_condition_instances,
            organization=organization,
            organization_priority=organization_priority,
            workspace=workspace,
            created=created,
            archived=archived,
            reconciliation_running=reconciliation_running,
            effective_criticality=effective_criticality,
            url=url,
            has_icon=has_icon,
            icon_url=icon_url,
            is_class_icon=is_class_icon,
            pop_count=pop_count,
            datasource_count=datasource_count,
            kind=kind,
            legal_name=legal_name,
            slug=slug,
            active=active,
            asn=asn,
            certifications=certifications,
        )

        provider_list.additional_properties = d
        return provider_list

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
