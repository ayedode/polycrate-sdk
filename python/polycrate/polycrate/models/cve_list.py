from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.effective_criticality_enum import EffectiveCriticalityEnum, check_effective_criticality_enum
from ..models.last_state_enum import LastStateEnum, check_last_state_enum

if TYPE_CHECKING:
    from ..models.cve_list_active_condition_instances_item import CVEListActiveConditionInstancesItem
    from ..models.cve_list_created import CVEListCreated


T = TypeVar("T", bound="CVEList")


@_attrs_define
class CVEList:
    """List serializer for CVE - V2 Dynamic Tables. Global object — no organization/workspace.

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
        active_condition_instances (list[CVEListActiveConditionInstancesItem]):
        organization (None | str):
        organization_priority (bool): True when the object's organization has priority=True.
        workspace (None | str):
        created (CVEListCreated):
        archived (bool): Archived objects are not shown in the UI and are not managed by the API.
        reconciliation_running (bool):
        effective_criticality (EffectiveCriticalityEnum | None):
        url (str): Gibt die absolute URL zum Object zurück.
        cve_id (str):
        title (str):
        severity (str):
        status (str):
        cvss_score (None | str):
        published_at (datetime.datetime | None):
        findings_count (int):
        has_kev (bool): Whether this CVE has a CISA KEV (Known Exploited Vulnerabilities) source record.
    """

    id: UUID
    name: str
    state: LastStateEnum
    labels: Any
    conditions: Any
    condition_instance_count: int
    active_condition_instances: list[CVEListActiveConditionInstancesItem]
    organization: None | str
    organization_priority: bool
    workspace: None | str
    created: CVEListCreated
    archived: bool
    reconciliation_running: bool
    effective_criticality: EffectiveCriticalityEnum | None
    url: str
    cve_id: str
    title: str
    severity: str
    status: str
    cvss_score: None | str
    published_at: datetime.datetime | None
    findings_count: int
    has_kev: bool
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

        cve_id = self.cve_id

        title = self.title

        severity = self.severity

        status = self.status

        cvss_score: None | str
        cvss_score = self.cvss_score

        published_at: None | str
        if isinstance(self.published_at, datetime.datetime):
            published_at = self.published_at.isoformat()
        else:
            published_at = self.published_at

        findings_count = self.findings_count

        has_kev = self.has_kev

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
                "cve_id": cve_id,
                "title": title,
                "severity": severity,
                "status": status,
                "cvss_score": cvss_score,
                "published_at": published_at,
                "findings_count": findings_count,
                "has_kev": has_kev,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.cve_list_active_condition_instances_item import (
            CVEListActiveConditionInstancesItem,  # noqa: PLC0415
        )
        from ..models.cve_list_created import CVEListCreated  # noqa: PLC0415

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
            active_condition_instances_item = CVEListActiveConditionInstancesItem.from_dict(
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

        created = CVEListCreated.from_dict(d.pop("created"))

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

        cve_id = d.pop("cve_id")

        title = d.pop("title")

        severity = d.pop("severity")

        status = d.pop("status")

        def _parse_cvss_score(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        cvss_score = _parse_cvss_score(d.pop("cvss_score"))

        def _parse_published_at(data: object) -> datetime.datetime | None:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                published_at_type_0 = datetime.datetime.fromisoformat(data)

                return published_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None, data)

        published_at = _parse_published_at(d.pop("published_at"))

        findings_count = d.pop("findings_count")

        has_kev = d.pop("has_kev")

        cve_list = cls(
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
            cve_id=cve_id,
            title=title,
            severity=severity,
            status=status,
            cvss_score=cvss_score,
            published_at=published_at,
            findings_count=findings_count,
            has_kev=has_kev,
        )

        cve_list.additional_properties = d
        return cve_list

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
