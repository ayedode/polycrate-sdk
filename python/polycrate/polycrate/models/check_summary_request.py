from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="CheckSummaryRequest")


@_attrs_define
class CheckSummaryRequest:
    """Serializer for check execution summary in health submission.

    Aggregated statistics about checks performed by the agent.

    Per .specs/0.11.9/index.md - Sektion 4

        Attributes:
            monitored_endpoints (int | Unset): Number of endpoints this agent is monitoring Default: 0.
            checks_per_minute (float | Unset): Current check rate (checks/min) Default: 0.0.
            checks_in_queue (int | Unset): Checks waiting to be executed Default: 0.
            failed_checks (int | Unset): Total failed checks since agent start Default: 0.
            successful_checks (int | Unset): Total successful checks since agent start Default: 0.
            checks_since_last_report (int | Unset): Checks executed since last health report Default: 0.
            total_checks (int | Unset): Total checks executed since agent start Default: 0.
    """

    monitored_endpoints: int | Unset = 0
    checks_per_minute: float | Unset = 0.0
    checks_in_queue: int | Unset = 0
    failed_checks: int | Unset = 0
    successful_checks: int | Unset = 0
    checks_since_last_report: int | Unset = 0
    total_checks: int | Unset = 0
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        monitored_endpoints = self.monitored_endpoints

        checks_per_minute = self.checks_per_minute

        checks_in_queue = self.checks_in_queue

        failed_checks = self.failed_checks

        successful_checks = self.successful_checks

        checks_since_last_report = self.checks_since_last_report

        total_checks = self.total_checks

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if monitored_endpoints is not UNSET:
            field_dict["monitored_endpoints"] = monitored_endpoints
        if checks_per_minute is not UNSET:
            field_dict["checks_per_minute"] = checks_per_minute
        if checks_in_queue is not UNSET:
            field_dict["checks_in_queue"] = checks_in_queue
        if failed_checks is not UNSET:
            field_dict["failed_checks"] = failed_checks
        if successful_checks is not UNSET:
            field_dict["successful_checks"] = successful_checks
        if checks_since_last_report is not UNSET:
            field_dict["checks_since_last_report"] = checks_since_last_report
        if total_checks is not UNSET:
            field_dict["total_checks"] = total_checks

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        monitored_endpoints = d.pop("monitored_endpoints", UNSET)

        checks_per_minute = d.pop("checks_per_minute", UNSET)

        checks_in_queue = d.pop("checks_in_queue", UNSET)

        failed_checks = d.pop("failed_checks", UNSET)

        successful_checks = d.pop("successful_checks", UNSET)

        checks_since_last_report = d.pop("checks_since_last_report", UNSET)

        total_checks = d.pop("total_checks", UNSET)

        check_summary_request = cls(
            monitored_endpoints=monitored_endpoints,
            checks_per_minute=checks_per_minute,
            checks_in_queue=checks_in_queue,
            failed_checks=failed_checks,
            successful_checks=successful_checks,
            checks_since_last_report=checks_since_last_report,
            total_checks=total_checks,
        )

        check_summary_request.additional_properties = d
        return check_summary_request

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
