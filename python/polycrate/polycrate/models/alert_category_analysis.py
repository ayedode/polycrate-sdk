from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="AlertCategoryAnalysis")


@_attrs_define
class AlertCategoryAnalysis:
    """
    Attributes:
        id (int):
        category (UUID):
        category_name (str):
        category_label (str):
        alertname (str):
        signal_class (str):
        rationale (str):
        suggested_actions (Any):
        confidence (float):
        confidence_threshold (float):
        below_threshold (bool):
        snapshot (Any):
        triggered_by (str):
        organization_id (str):
        workspace_id (str):
        analyzed_at (datetime.datetime):
        created_at (datetime.datetime):
    """

    id: int
    category: UUID
    category_name: str
    category_label: str
    alertname: str
    signal_class: str
    rationale: str
    suggested_actions: Any
    confidence: float
    confidence_threshold: float
    below_threshold: bool
    snapshot: Any
    triggered_by: str
    organization_id: str
    workspace_id: str
    analyzed_at: datetime.datetime
    created_at: datetime.datetime
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        category = str(self.category)

        category_name = self.category_name

        category_label = self.category_label

        alertname = self.alertname

        signal_class = self.signal_class

        rationale = self.rationale

        suggested_actions = self.suggested_actions

        confidence = self.confidence

        confidence_threshold = self.confidence_threshold

        below_threshold = self.below_threshold

        snapshot = self.snapshot

        triggered_by = self.triggered_by

        organization_id = self.organization_id

        workspace_id = self.workspace_id

        analyzed_at = self.analyzed_at.isoformat()

        created_at = self.created_at.isoformat()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "category": category,
                "category_name": category_name,
                "category_label": category_label,
                "alertname": alertname,
                "signal_class": signal_class,
                "rationale": rationale,
                "suggested_actions": suggested_actions,
                "confidence": confidence,
                "confidence_threshold": confidence_threshold,
                "below_threshold": below_threshold,
                "snapshot": snapshot,
                "triggered_by": triggered_by,
                "organization_id": organization_id,
                "workspace_id": workspace_id,
                "analyzed_at": analyzed_at,
                "created_at": created_at,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        category = UUID(d.pop("category"))

        category_name = d.pop("category_name")

        category_label = d.pop("category_label")

        alertname = d.pop("alertname")

        signal_class = d.pop("signal_class")

        rationale = d.pop("rationale")

        suggested_actions = d.pop("suggested_actions")

        confidence = d.pop("confidence")

        confidence_threshold = d.pop("confidence_threshold")

        below_threshold = d.pop("below_threshold")

        snapshot = d.pop("snapshot")

        triggered_by = d.pop("triggered_by")

        organization_id = d.pop("organization_id")

        workspace_id = d.pop("workspace_id")

        analyzed_at = datetime.datetime.fromisoformat(d.pop("analyzed_at"))

        created_at = datetime.datetime.fromisoformat(d.pop("created_at"))

        alert_category_analysis = cls(
            id=id,
            category=category,
            category_name=category_name,
            category_label=category_label,
            alertname=alertname,
            signal_class=signal_class,
            rationale=rationale,
            suggested_actions=suggested_actions,
            confidence=confidence,
            confidence_threshold=confidence_threshold,
            below_threshold=below_threshold,
            snapshot=snapshot,
            triggered_by=triggered_by,
            organization_id=organization_id,
            workspace_id=workspace_id,
            analyzed_at=analyzed_at,
            created_at=created_at,
        )

        alert_category_analysis.additional_properties = d
        return alert_category_analysis

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
