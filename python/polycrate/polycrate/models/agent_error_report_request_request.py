from __future__ import annotations

import datetime
import json
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from .. import types

if TYPE_CHECKING:
    from ..models.agent_error_report_request_request_error_counts import AgentErrorReportRequestRequestErrorCounts
    from ..models.agent_error_report_request_request_recent_errors_item import (
        AgentErrorReportRequestRequestRecentErrorsItem,
    )
    from ..models.agent_error_report_request_request_system_info import AgentErrorReportRequestRequestSystemInfo


T = TypeVar("T", bound="AgentErrorReportRequestRequest")


@_attrs_define
class AgentErrorReportRequestRequest:
    """
    Attributes:
        agent_id (str): Agent-reported ID
        timestamp (datetime.datetime): Timestamp of the error report
        total_errors (int): Total number of errors
        error_counts (AgentErrorReportRequestRequestErrorCounts): Error counts by category
        critical_errors (list[str]): List of critical error messages
        recent_errors (list[AgentErrorReportRequestRequestRecentErrorsItem]): List of recent error objects
        system_info (AgentErrorReportRequestRequestSystemInfo): System information at error time
    """

    agent_id: str
    timestamp: datetime.datetime
    total_errors: int
    error_counts: AgentErrorReportRequestRequestErrorCounts
    critical_errors: list[str]
    recent_errors: list[AgentErrorReportRequestRequestRecentErrorsItem]
    system_info: AgentErrorReportRequestRequestSystemInfo
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        agent_id = self.agent_id

        timestamp = self.timestamp.isoformat()

        total_errors = self.total_errors

        error_counts = self.error_counts.to_dict()

        critical_errors = self.critical_errors

        recent_errors = []
        for recent_errors_item_data in self.recent_errors:
            recent_errors_item = recent_errors_item_data.to_dict()
            recent_errors.append(recent_errors_item)

        system_info = self.system_info.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "agent_id": agent_id,
                "timestamp": timestamp,
                "total_errors": total_errors,
                "error_counts": error_counts,
                "critical_errors": critical_errors,
                "recent_errors": recent_errors,
                "system_info": system_info,
            }
        )

        return field_dict

    def to_multipart(self) -> types.RequestFiles:
        files: types.RequestFiles = []

        files.append(("agent_id", (None, str(self.agent_id).encode(), "text/plain")))

        files.append(("timestamp", (None, self.timestamp.isoformat().encode(), "text/plain")))

        files.append(("total_errors", (None, str(self.total_errors).encode(), "text/plain")))

        files.append(("error_counts", (None, json.dumps(self.error_counts.to_dict()).encode(), "application/json")))

        for critical_errors_item_element in self.critical_errors:
            files.append(("critical_errors", (None, str(critical_errors_item_element).encode(), "text/plain")))

        for recent_errors_item_element in self.recent_errors:
            files.append(
                ("recent_errors", (None, json.dumps(recent_errors_item_element.to_dict()).encode(), "application/json"))
            )

        files.append(("system_info", (None, json.dumps(self.system_info.to_dict()).encode(), "application/json")))

        for prop_name, prop in self.additional_properties.items():
            files.append((prop_name, (None, str(prop).encode(), "text/plain")))

        return files

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.agent_error_report_request_request_error_counts import (
            AgentErrorReportRequestRequestErrorCounts,  # noqa: PLC0415
        )
        from ..models.agent_error_report_request_request_recent_errors_item import (
            AgentErrorReportRequestRequestRecentErrorsItem,  # noqa: PLC0415
        )
        from ..models.agent_error_report_request_request_system_info import (
            AgentErrorReportRequestRequestSystemInfo,  # noqa: PLC0415
        )

        d = dict(src_dict)
        agent_id = d.pop("agent_id")

        timestamp = datetime.datetime.fromisoformat(d.pop("timestamp"))

        total_errors = d.pop("total_errors")

        error_counts = AgentErrorReportRequestRequestErrorCounts.from_dict(d.pop("error_counts"))

        critical_errors = cast(list[str], d.pop("critical_errors"))

        recent_errors = []
        _recent_errors = d.pop("recent_errors")
        for recent_errors_item_data in _recent_errors:
            recent_errors_item = AgentErrorReportRequestRequestRecentErrorsItem.from_dict(recent_errors_item_data)

            recent_errors.append(recent_errors_item)

        system_info = AgentErrorReportRequestRequestSystemInfo.from_dict(d.pop("system_info"))

        agent_error_report_request_request = cls(
            agent_id=agent_id,
            timestamp=timestamp,
            total_errors=total_errors,
            error_counts=error_counts,
            critical_errors=critical_errors,
            recent_errors=recent_errors,
            system_info=system_info,
        )

        agent_error_report_request_request.additional_properties = d
        return agent_error_report_request_request

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
