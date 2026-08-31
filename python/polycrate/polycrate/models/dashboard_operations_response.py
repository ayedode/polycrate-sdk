from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.dashboard_operations_response_blocked_rollouts import DashboardOperationsResponseBlockedRollouts
    from ..models.dashboard_operations_response_endpoints_not_ok import DashboardOperationsResponseEndpointsNotOk
    from ..models.dashboard_operations_response_expired_certificates import (
        DashboardOperationsResponseExpiredCertificates,
    )
    from ..models.dashboard_operations_response_k8s_clusters_not_ok import DashboardOperationsResponseK8SClustersNotOk
    from ..models.dashboard_operations_response_last_ssh_sessions import DashboardOperationsResponseLastSshSessions
    from ..models.dashboard_operations_response_overdue_backup_schedules import (
        DashboardOperationsResponseOverdueBackupSchedules,
    )
    from ..models.dashboard_operations_response_recent_alerts import DashboardOperationsResponseRecentAlerts
    from ..models.dashboard_operations_response_recent_downtimes import DashboardOperationsResponseRecentDowntimes
    from ..models.dashboard_operations_response_recent_maintenances import DashboardOperationsResponseRecentMaintenances
    from ..models.dashboard_operations_response_workspaces_not_ok import DashboardOperationsResponseWorkspacesNotOk


T = TypeVar("T", bound="DashboardOperationsResponse")


@_attrs_define
class DashboardOperationsResponse:
    """
    Attributes:
        updated_at (datetime.datetime):
        workspaces_not_ok (DashboardOperationsResponseWorkspacesNotOk):
        endpoints_not_ok (DashboardOperationsResponseEndpointsNotOk):
        recent_downtimes (DashboardOperationsResponseRecentDowntimes):
        recent_maintenances (DashboardOperationsResponseRecentMaintenances):
        blocked_rollouts (DashboardOperationsResponseBlockedRollouts):
        last_ssh_sessions (DashboardOperationsResponseLastSshSessions):
        recent_alerts (DashboardOperationsResponseRecentAlerts):
        k8s_clusters_not_ok (DashboardOperationsResponseK8SClustersNotOk):
        overdue_backup_schedules (DashboardOperationsResponseOverdueBackupSchedules):
        expired_certificates (DashboardOperationsResponseExpiredCertificates):
    """

    updated_at: datetime.datetime
    workspaces_not_ok: DashboardOperationsResponseWorkspacesNotOk
    endpoints_not_ok: DashboardOperationsResponseEndpointsNotOk
    recent_downtimes: DashboardOperationsResponseRecentDowntimes
    recent_maintenances: DashboardOperationsResponseRecentMaintenances
    blocked_rollouts: DashboardOperationsResponseBlockedRollouts
    last_ssh_sessions: DashboardOperationsResponseLastSshSessions
    recent_alerts: DashboardOperationsResponseRecentAlerts
    k8s_clusters_not_ok: DashboardOperationsResponseK8SClustersNotOk
    overdue_backup_schedules: DashboardOperationsResponseOverdueBackupSchedules
    expired_certificates: DashboardOperationsResponseExpiredCertificates
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        updated_at = self.updated_at.isoformat()

        workspaces_not_ok = self.workspaces_not_ok.to_dict()

        endpoints_not_ok = self.endpoints_not_ok.to_dict()

        recent_downtimes = self.recent_downtimes.to_dict()

        recent_maintenances = self.recent_maintenances.to_dict()

        blocked_rollouts = self.blocked_rollouts.to_dict()

        last_ssh_sessions = self.last_ssh_sessions.to_dict()

        recent_alerts = self.recent_alerts.to_dict()

        k8s_clusters_not_ok = self.k8s_clusters_not_ok.to_dict()

        overdue_backup_schedules = self.overdue_backup_schedules.to_dict()

        expired_certificates = self.expired_certificates.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "updated_at": updated_at,
                "workspaces_not_ok": workspaces_not_ok,
                "endpoints_not_ok": endpoints_not_ok,
                "recent_downtimes": recent_downtimes,
                "recent_maintenances": recent_maintenances,
                "blocked_rollouts": blocked_rollouts,
                "last_ssh_sessions": last_ssh_sessions,
                "recent_alerts": recent_alerts,
                "k8s_clusters_not_ok": k8s_clusters_not_ok,
                "overdue_backup_schedules": overdue_backup_schedules,
                "expired_certificates": expired_certificates,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.dashboard_operations_response_blocked_rollouts import DashboardOperationsResponseBlockedRollouts
        from ..models.dashboard_operations_response_endpoints_not_ok import DashboardOperationsResponseEndpointsNotOk
        from ..models.dashboard_operations_response_expired_certificates import (
            DashboardOperationsResponseExpiredCertificates,
        )
        from ..models.dashboard_operations_response_k8s_clusters_not_ok import (
            DashboardOperationsResponseK8SClustersNotOk,
        )
        from ..models.dashboard_operations_response_last_ssh_sessions import DashboardOperationsResponseLastSshSessions
        from ..models.dashboard_operations_response_overdue_backup_schedules import (
            DashboardOperationsResponseOverdueBackupSchedules,
        )
        from ..models.dashboard_operations_response_recent_alerts import DashboardOperationsResponseRecentAlerts
        from ..models.dashboard_operations_response_recent_downtimes import DashboardOperationsResponseRecentDowntimes
        from ..models.dashboard_operations_response_recent_maintenances import (
            DashboardOperationsResponseRecentMaintenances,
        )
        from ..models.dashboard_operations_response_workspaces_not_ok import DashboardOperationsResponseWorkspacesNotOk

        d = dict(src_dict)
        updated_at = datetime.datetime.fromisoformat(d.pop("updated_at"))

        workspaces_not_ok = DashboardOperationsResponseWorkspacesNotOk.from_dict(d.pop("workspaces_not_ok"))

        endpoints_not_ok = DashboardOperationsResponseEndpointsNotOk.from_dict(d.pop("endpoints_not_ok"))

        recent_downtimes = DashboardOperationsResponseRecentDowntimes.from_dict(d.pop("recent_downtimes"))

        recent_maintenances = DashboardOperationsResponseRecentMaintenances.from_dict(d.pop("recent_maintenances"))

        blocked_rollouts = DashboardOperationsResponseBlockedRollouts.from_dict(d.pop("blocked_rollouts"))

        last_ssh_sessions = DashboardOperationsResponseLastSshSessions.from_dict(d.pop("last_ssh_sessions"))

        recent_alerts = DashboardOperationsResponseRecentAlerts.from_dict(d.pop("recent_alerts"))

        k8s_clusters_not_ok = DashboardOperationsResponseK8SClustersNotOk.from_dict(d.pop("k8s_clusters_not_ok"))

        overdue_backup_schedules = DashboardOperationsResponseOverdueBackupSchedules.from_dict(
            d.pop("overdue_backup_schedules")
        )

        expired_certificates = DashboardOperationsResponseExpiredCertificates.from_dict(d.pop("expired_certificates"))

        dashboard_operations_response = cls(
            updated_at=updated_at,
            workspaces_not_ok=workspaces_not_ok,
            endpoints_not_ok=endpoints_not_ok,
            recent_downtimes=recent_downtimes,
            recent_maintenances=recent_maintenances,
            blocked_rollouts=blocked_rollouts,
            last_ssh_sessions=last_ssh_sessions,
            recent_alerts=recent_alerts,
            k8s_clusters_not_ok=k8s_clusters_not_ok,
            overdue_backup_schedules=overdue_backup_schedules,
            expired_certificates=expired_certificates,
        )

        dashboard_operations_response.additional_properties = d
        return dashboard_operations_response

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
