from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.organization_cached_metrics_active import OrganizationCachedMetricsActive
    from ..models.organization_cached_metrics_alerts import OrganizationCachedMetricsAlerts
    from ..models.organization_cached_metrics_costs import OrganizationCachedMetricsCosts
    from ..models.organization_cached_metrics_endpoints import OrganizationCachedMetricsEndpoints
    from ..models.organization_cached_metrics_loadbalancers import OrganizationCachedMetricsLoadbalancers
    from ..models.organization_cached_metrics_members import OrganizationCachedMetricsMembers
    from ..models.organization_cached_metrics_message import OrganizationCachedMetricsMessage
    from ..models.organization_cached_metrics_open import OrganizationCachedMetricsOpen
    from ..models.organization_cached_metrics_s3 import OrganizationCachedMetricsS3
    from ..models.organization_cached_metrics_total import OrganizationCachedMetricsTotal
    from ..models.organization_cached_metrics_volumes import OrganizationCachedMetricsVolumes


T = TypeVar("T", bound="OrganizationCachedMetrics")


@_attrs_define
class OrganizationCachedMetrics:
    """Customer Portal org dashboard payload from cached_* fields (Spec 630).

    Nested object shapes are explicit so OpenAPI / generated clients stay typed.

        Attributes:
            organization_id (UUID): Organization UUID (same as path id)
            updated_at (datetime.datetime | None): Last time cached_* rollups were refreshed by the metrics beat
            k8s_clusters (OrganizationCachedMetricsTotal): Single total count bucket (Spec 630).
            workspaces (OrganizationCachedMetricsTotal): Single total count bucket (Spec 630).
            endpoints (OrganizationCachedMetricsEndpoints): Endpoint rollup; ok = total - down (Spec 630).
            costs (OrganizationCachedMetricsCosts):
            members (OrganizationCachedMetricsMembers):
            maintenances (OrganizationCachedMetricsActive):
            incidents (OrganizationCachedMetricsOpen):
            downtimes (OrganizationCachedMetricsActive):
            s3 (OrganizationCachedMetricsS3):
            loadbalancers (OrganizationCachedMetricsLoadbalancers):
            volumes (OrganizationCachedMetricsVolumes):
            alerts (OrganizationCachedMetricsAlerts):
            messages (list[OrganizationCachedMetricsMessage]): Live ops messages (max 10), not from the cache beat
    """

    organization_id: UUID
    updated_at: datetime.datetime | None
    k8s_clusters: OrganizationCachedMetricsTotal
    workspaces: OrganizationCachedMetricsTotal
    endpoints: OrganizationCachedMetricsEndpoints
    costs: OrganizationCachedMetricsCosts
    members: OrganizationCachedMetricsMembers
    maintenances: OrganizationCachedMetricsActive
    incidents: OrganizationCachedMetricsOpen
    downtimes: OrganizationCachedMetricsActive
    s3: OrganizationCachedMetricsS3
    loadbalancers: OrganizationCachedMetricsLoadbalancers
    volumes: OrganizationCachedMetricsVolumes
    alerts: OrganizationCachedMetricsAlerts
    messages: list[OrganizationCachedMetricsMessage]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        organization_id = str(self.organization_id)

        updated_at: None | str
        if isinstance(self.updated_at, datetime.datetime):
            updated_at = self.updated_at.isoformat()
        else:
            updated_at = self.updated_at

        k8s_clusters = self.k8s_clusters.to_dict()

        workspaces = self.workspaces.to_dict()

        endpoints = self.endpoints.to_dict()

        costs = self.costs.to_dict()

        members = self.members.to_dict()

        maintenances = self.maintenances.to_dict()

        incidents = self.incidents.to_dict()

        downtimes = self.downtimes.to_dict()

        s3 = self.s3.to_dict()

        loadbalancers = self.loadbalancers.to_dict()

        volumes = self.volumes.to_dict()

        alerts = self.alerts.to_dict()

        messages = []
        for messages_item_data in self.messages:
            messages_item = messages_item_data.to_dict()
            messages.append(messages_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "organization_id": organization_id,
                "updated_at": updated_at,
                "k8s_clusters": k8s_clusters,
                "workspaces": workspaces,
                "endpoints": endpoints,
                "costs": costs,
                "members": members,
                "maintenances": maintenances,
                "incidents": incidents,
                "downtimes": downtimes,
                "s3": s3,
                "loadbalancers": loadbalancers,
                "volumes": volumes,
                "alerts": alerts,
                "messages": messages,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.organization_cached_metrics_active import OrganizationCachedMetricsActive
        from ..models.organization_cached_metrics_alerts import OrganizationCachedMetricsAlerts
        from ..models.organization_cached_metrics_costs import OrganizationCachedMetricsCosts
        from ..models.organization_cached_metrics_endpoints import OrganizationCachedMetricsEndpoints
        from ..models.organization_cached_metrics_loadbalancers import OrganizationCachedMetricsLoadbalancers
        from ..models.organization_cached_metrics_members import OrganizationCachedMetricsMembers
        from ..models.organization_cached_metrics_message import OrganizationCachedMetricsMessage
        from ..models.organization_cached_metrics_open import OrganizationCachedMetricsOpen
        from ..models.organization_cached_metrics_s3 import OrganizationCachedMetricsS3
        from ..models.organization_cached_metrics_total import OrganizationCachedMetricsTotal
        from ..models.organization_cached_metrics_volumes import OrganizationCachedMetricsVolumes

        d = dict(src_dict)
        organization_id = UUID(d.pop("organization_id"))

        def _parse_updated_at(data: object) -> datetime.datetime | None:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                updated_at_type_0 = datetime.datetime.fromisoformat(data)

                return updated_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None, data)

        updated_at = _parse_updated_at(d.pop("updated_at"))

        k8s_clusters = OrganizationCachedMetricsTotal.from_dict(d.pop("k8s_clusters"))

        workspaces = OrganizationCachedMetricsTotal.from_dict(d.pop("workspaces"))

        endpoints = OrganizationCachedMetricsEndpoints.from_dict(d.pop("endpoints"))

        costs = OrganizationCachedMetricsCosts.from_dict(d.pop("costs"))

        members = OrganizationCachedMetricsMembers.from_dict(d.pop("members"))

        maintenances = OrganizationCachedMetricsActive.from_dict(d.pop("maintenances"))

        incidents = OrganizationCachedMetricsOpen.from_dict(d.pop("incidents"))

        downtimes = OrganizationCachedMetricsActive.from_dict(d.pop("downtimes"))

        s3 = OrganizationCachedMetricsS3.from_dict(d.pop("s3"))

        loadbalancers = OrganizationCachedMetricsLoadbalancers.from_dict(d.pop("loadbalancers"))

        volumes = OrganizationCachedMetricsVolumes.from_dict(d.pop("volumes"))

        alerts = OrganizationCachedMetricsAlerts.from_dict(d.pop("alerts"))

        messages = []
        _messages = d.pop("messages")
        for messages_item_data in _messages:
            messages_item = OrganizationCachedMetricsMessage.from_dict(messages_item_data)

            messages.append(messages_item)

        organization_cached_metrics = cls(
            organization_id=organization_id,
            updated_at=updated_at,
            k8s_clusters=k8s_clusters,
            workspaces=workspaces,
            endpoints=endpoints,
            costs=costs,
            members=members,
            maintenances=maintenances,
            incidents=incidents,
            downtimes=downtimes,
            s3=s3,
            loadbalancers=loadbalancers,
            volumes=volumes,
            alerts=alerts,
            messages=messages,
        )

        organization_cached_metrics.additional_properties = d
        return organization_cached_metrics

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
