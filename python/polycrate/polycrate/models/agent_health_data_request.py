from __future__ import annotations

import datetime
import json
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from .. import types
from ..models.agent_health_data_status_enum import AgentHealthDataStatusEnum, check_agent_health_data_status_enum
from ..models.agent_kind_enum import AgentKindEnum, check_agent_kind_enum
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.check_result_input_request import CheckResultInputRequest
    from ..models.check_summary_request import CheckSummaryRequest


T = TypeVar("T", bound="AgentHealthDataRequest")


@_attrs_define
class AgentHealthDataRequest:
    """Serializer for agents to submit health data.

    Extended in 0.11.9 to accept check_summary and check_results.
    Now writes directly to Agent model instead of creating AgentHealthData.

    Per .specs/0.11.9/index.md - Sektion 4

        Attributes:
            reported_agent_id (str | Unset): Agent-reported unique identifier
            version (str | Unset): Agent software version
            kind (AgentKindEnum | Unset): * `agent` - Agent
                * `operator` - Operator
            status (AgentHealthDataStatusEnum | Unset): * `healthy` - healthy
                * `degraded` - degraded
                * `unhealthy` - unhealthy
                * `critical` - critical Default: 'healthy'.
            uptime_seconds (int | Unset):
            start_time (datetime.datetime | Unset):
            last_config_update (datetime.datetime | Unset):
            config_version (str | Unset):
            storage_healthy (bool | Unset):  Default: True.
            api_connected (bool | Unset):  Default: True.
            reported_at (datetime.datetime | Unset):
            resource_metrics (Any | Unset):
            network_metrics (Any | Unset):
            check_metrics (Any | Unset):
            error_counts (Any | Unset):
            warnings (list[str] | Unset):
            critical_errors (list[str] | Unset):
            system_info (Any | Unset):
            storage_stats (Any | Unset):
            agent_configuration (Any | Unset):
            check_summary (CheckSummaryRequest | Unset): Serializer for check execution summary in health submission.

                Aggregated statistics about checks performed by the agent.

                Per .specs/0.11.9/index.md - Sektion 4
            check_results (list[CheckResultInputRequest] | Unset):
    """

    reported_agent_id: str | Unset = UNSET
    version: str | Unset = UNSET
    kind: AgentKindEnum | Unset = UNSET
    status: AgentHealthDataStatusEnum | Unset = "healthy"
    uptime_seconds: int | Unset = UNSET
    start_time: datetime.datetime | Unset = UNSET
    last_config_update: datetime.datetime | Unset = UNSET
    config_version: str | Unset = UNSET
    storage_healthy: bool | Unset = True
    api_connected: bool | Unset = True
    reported_at: datetime.datetime | Unset = UNSET
    resource_metrics: Any | Unset = UNSET
    network_metrics: Any | Unset = UNSET
    check_metrics: Any | Unset = UNSET
    error_counts: Any | Unset = UNSET
    warnings: list[str] | Unset = UNSET
    critical_errors: list[str] | Unset = UNSET
    system_info: Any | Unset = UNSET
    storage_stats: Any | Unset = UNSET
    agent_configuration: Any | Unset = UNSET
    check_summary: CheckSummaryRequest | Unset = UNSET
    check_results: list[CheckResultInputRequest] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        reported_agent_id = self.reported_agent_id

        version = self.version

        kind: str | Unset = UNSET
        if not isinstance(self.kind, Unset):
            kind = self.kind

        status: str | Unset = UNSET
        if not isinstance(self.status, Unset):
            status = self.status

        uptime_seconds = self.uptime_seconds

        start_time: str | Unset = UNSET
        if not isinstance(self.start_time, Unset):
            start_time = self.start_time.isoformat()

        last_config_update: str | Unset = UNSET
        if not isinstance(self.last_config_update, Unset):
            last_config_update = self.last_config_update.isoformat()

        config_version = self.config_version

        storage_healthy = self.storage_healthy

        api_connected = self.api_connected

        reported_at: str | Unset = UNSET
        if not isinstance(self.reported_at, Unset):
            reported_at = self.reported_at.isoformat()

        resource_metrics = self.resource_metrics

        network_metrics = self.network_metrics

        check_metrics = self.check_metrics

        error_counts = self.error_counts

        warnings: list[str] | Unset = UNSET
        if not isinstance(self.warnings, Unset):
            warnings = self.warnings

        critical_errors: list[str] | Unset = UNSET
        if not isinstance(self.critical_errors, Unset):
            critical_errors = self.critical_errors

        system_info = self.system_info

        storage_stats = self.storage_stats

        agent_configuration = self.agent_configuration

        check_summary: dict[str, Any] | Unset = UNSET
        if not isinstance(self.check_summary, Unset):
            check_summary = self.check_summary.to_dict()

        check_results: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.check_results, Unset):
            check_results = []
            for check_results_item_data in self.check_results:
                check_results_item = check_results_item_data.to_dict()
                check_results.append(check_results_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if reported_agent_id is not UNSET:
            field_dict["reported_agent_id"] = reported_agent_id
        if version is not UNSET:
            field_dict["version"] = version
        if kind is not UNSET:
            field_dict["kind"] = kind
        if status is not UNSET:
            field_dict["status"] = status
        if uptime_seconds is not UNSET:
            field_dict["uptime_seconds"] = uptime_seconds
        if start_time is not UNSET:
            field_dict["start_time"] = start_time
        if last_config_update is not UNSET:
            field_dict["last_config_update"] = last_config_update
        if config_version is not UNSET:
            field_dict["config_version"] = config_version
        if storage_healthy is not UNSET:
            field_dict["storage_healthy"] = storage_healthy
        if api_connected is not UNSET:
            field_dict["api_connected"] = api_connected
        if reported_at is not UNSET:
            field_dict["reported_at"] = reported_at
        if resource_metrics is not UNSET:
            field_dict["resource_metrics"] = resource_metrics
        if network_metrics is not UNSET:
            field_dict["network_metrics"] = network_metrics
        if check_metrics is not UNSET:
            field_dict["check_metrics"] = check_metrics
        if error_counts is not UNSET:
            field_dict["error_counts"] = error_counts
        if warnings is not UNSET:
            field_dict["warnings"] = warnings
        if critical_errors is not UNSET:
            field_dict["critical_errors"] = critical_errors
        if system_info is not UNSET:
            field_dict["system_info"] = system_info
        if storage_stats is not UNSET:
            field_dict["storage_stats"] = storage_stats
        if agent_configuration is not UNSET:
            field_dict["agent_configuration"] = agent_configuration
        if check_summary is not UNSET:
            field_dict["check_summary"] = check_summary
        if check_results is not UNSET:
            field_dict["check_results"] = check_results

        return field_dict

    def to_multipart(self) -> types.RequestFiles:
        files: types.RequestFiles = []

        if not isinstance(self.reported_agent_id, Unset):
            files.append(("reported_agent_id", (None, str(self.reported_agent_id).encode(), "text/plain")))

        if not isinstance(self.version, Unset):
            files.append(("version", (None, str(self.version).encode(), "text/plain")))

        if not isinstance(self.kind, Unset):
            files.append(("kind", (None, str(self.kind).encode(), "text/plain")))

        if not isinstance(self.status, Unset):
            files.append(("status", (None, str(self.status).encode(), "text/plain")))

        if not isinstance(self.uptime_seconds, Unset):
            files.append(("uptime_seconds", (None, str(self.uptime_seconds).encode(), "text/plain")))

        if not isinstance(self.start_time, Unset):
            files.append(("start_time", (None, self.start_time.isoformat().encode(), "text/plain")))

        if not isinstance(self.last_config_update, Unset):
            files.append(("last_config_update", (None, self.last_config_update.isoformat().encode(), "text/plain")))

        if not isinstance(self.config_version, Unset):
            files.append(("config_version", (None, str(self.config_version).encode(), "text/plain")))

        if not isinstance(self.storage_healthy, Unset):
            files.append(("storage_healthy", (None, str(self.storage_healthy).encode(), "text/plain")))

        if not isinstance(self.api_connected, Unset):
            files.append(("api_connected", (None, str(self.api_connected).encode(), "text/plain")))

        if not isinstance(self.reported_at, Unset):
            files.append(("reported_at", (None, self.reported_at.isoformat().encode(), "text/plain")))

        if not isinstance(self.resource_metrics, Unset):
            files.append(("resource_metrics", (None, str(self.resource_metrics).encode(), "text/plain")))

        if not isinstance(self.network_metrics, Unset):
            files.append(("network_metrics", (None, str(self.network_metrics).encode(), "text/plain")))

        if not isinstance(self.check_metrics, Unset):
            files.append(("check_metrics", (None, str(self.check_metrics).encode(), "text/plain")))

        if not isinstance(self.error_counts, Unset):
            files.append(("error_counts", (None, str(self.error_counts).encode(), "text/plain")))

        if not isinstance(self.warnings, Unset):
            for warnings_item_element in self.warnings:
                files.append(("warnings", (None, str(warnings_item_element).encode(), "text/plain")))

        if not isinstance(self.critical_errors, Unset):
            for critical_errors_item_element in self.critical_errors:
                files.append(("critical_errors", (None, str(critical_errors_item_element).encode(), "text/plain")))

        if not isinstance(self.system_info, Unset):
            files.append(("system_info", (None, str(self.system_info).encode(), "text/plain")))

        if not isinstance(self.storage_stats, Unset):
            files.append(("storage_stats", (None, str(self.storage_stats).encode(), "text/plain")))

        if not isinstance(self.agent_configuration, Unset):
            files.append(("agent_configuration", (None, str(self.agent_configuration).encode(), "text/plain")))

        if not isinstance(self.check_summary, Unset):
            files.append(
                ("check_summary", (None, json.dumps(self.check_summary.to_dict()).encode(), "application/json"))
            )

        if not isinstance(self.check_results, Unset):
            for check_results_item_element in self.check_results:
                files.append(
                    (
                        "check_results",
                        (None, json.dumps(check_results_item_element.to_dict()).encode(), "application/json"),
                    )
                )

        for prop_name, prop in self.additional_properties.items():
            files.append((prop_name, (None, str(prop).encode(), "text/plain")))

        return files

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.check_result_input_request import CheckResultInputRequest
        from ..models.check_summary_request import CheckSummaryRequest

        d = dict(src_dict)
        reported_agent_id = d.pop("reported_agent_id", UNSET)

        version = d.pop("version", UNSET)

        _kind = d.pop("kind", UNSET)
        kind: AgentKindEnum | Unset
        if isinstance(_kind, Unset):
            kind = UNSET
        else:
            kind = check_agent_kind_enum(_kind)

        _status = d.pop("status", UNSET)
        status: AgentHealthDataStatusEnum | Unset
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = check_agent_health_data_status_enum(_status)

        uptime_seconds = d.pop("uptime_seconds", UNSET)

        _start_time = d.pop("start_time", UNSET)
        start_time: datetime.datetime | Unset
        if isinstance(_start_time, Unset):
            start_time = UNSET
        else:
            start_time = datetime.datetime.fromisoformat(_start_time)

        _last_config_update = d.pop("last_config_update", UNSET)
        last_config_update: datetime.datetime | Unset
        if isinstance(_last_config_update, Unset):
            last_config_update = UNSET
        else:
            last_config_update = datetime.datetime.fromisoformat(_last_config_update)

        config_version = d.pop("config_version", UNSET)

        storage_healthy = d.pop("storage_healthy", UNSET)

        api_connected = d.pop("api_connected", UNSET)

        _reported_at = d.pop("reported_at", UNSET)
        reported_at: datetime.datetime | Unset
        if isinstance(_reported_at, Unset):
            reported_at = UNSET
        else:
            reported_at = datetime.datetime.fromisoformat(_reported_at)

        resource_metrics = d.pop("resource_metrics", UNSET)

        network_metrics = d.pop("network_metrics", UNSET)

        check_metrics = d.pop("check_metrics", UNSET)

        error_counts = d.pop("error_counts", UNSET)

        warnings = cast(list[str], d.pop("warnings", UNSET))

        critical_errors = cast(list[str], d.pop("critical_errors", UNSET))

        system_info = d.pop("system_info", UNSET)

        storage_stats = d.pop("storage_stats", UNSET)

        agent_configuration = d.pop("agent_configuration", UNSET)

        _check_summary = d.pop("check_summary", UNSET)
        check_summary: CheckSummaryRequest | Unset
        if isinstance(_check_summary, Unset):
            check_summary = UNSET
        else:
            check_summary = CheckSummaryRequest.from_dict(_check_summary)

        _check_results = d.pop("check_results", UNSET)
        check_results: list[CheckResultInputRequest] | Unset = UNSET
        if _check_results is not UNSET:
            check_results = []
            for check_results_item_data in _check_results:
                check_results_item = CheckResultInputRequest.from_dict(check_results_item_data)

                check_results.append(check_results_item)

        agent_health_data_request = cls(
            reported_agent_id=reported_agent_id,
            version=version,
            kind=kind,
            status=status,
            uptime_seconds=uptime_seconds,
            start_time=start_time,
            last_config_update=last_config_update,
            config_version=config_version,
            storage_healthy=storage_healthy,
            api_connected=api_connected,
            reported_at=reported_at,
            resource_metrics=resource_metrics,
            network_metrics=network_metrics,
            check_metrics=check_metrics,
            error_counts=error_counts,
            warnings=warnings,
            critical_errors=critical_errors,
            system_info=system_info,
            storage_stats=storage_stats,
            agent_configuration=agent_configuration,
            check_summary=check_summary,
            check_results=check_results,
        )

        agent_health_data_request.additional_properties = d
        return agent_health_data_request

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
