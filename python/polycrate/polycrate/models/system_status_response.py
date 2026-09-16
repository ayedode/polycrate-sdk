from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.system_status_response_celery import SystemStatusResponseCelery
    from ..models.system_status_response_config import SystemStatusResponseConfig
    from ..models.system_status_response_integrations import SystemStatusResponseIntegrations
    from ..models.system_status_response_state import SystemStatusResponseState
    from ..models.system_status_response_uptime import SystemStatusResponseUptime


T = TypeVar("T", bound="SystemStatusResponse")


@_attrs_define
class SystemStatusResponse:
    """
    Attributes:
        timestamp (datetime.datetime):
        state (SystemStatusResponseState):
        config (SystemStatusResponseConfig):
        celery (SystemStatusResponseCelery):
        integrations (SystemStatusResponseIntegrations):
        uptime (SystemStatusResponseUptime):
    """

    timestamp: datetime.datetime
    state: SystemStatusResponseState
    config: SystemStatusResponseConfig
    celery: SystemStatusResponseCelery
    integrations: SystemStatusResponseIntegrations
    uptime: SystemStatusResponseUptime
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        timestamp = self.timestamp.isoformat()

        state = self.state.to_dict()

        config = self.config.to_dict()

        celery = self.celery.to_dict()

        integrations = self.integrations.to_dict()

        uptime = self.uptime.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "timestamp": timestamp,
                "state": state,
                "config": config,
                "celery": celery,
                "integrations": integrations,
                "uptime": uptime,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.system_status_response_celery import SystemStatusResponseCelery  # noqa: PLC0415
        from ..models.system_status_response_config import SystemStatusResponseConfig  # noqa: PLC0415
        from ..models.system_status_response_integrations import SystemStatusResponseIntegrations  # noqa: PLC0415
        from ..models.system_status_response_state import SystemStatusResponseState  # noqa: PLC0415
        from ..models.system_status_response_uptime import SystemStatusResponseUptime  # noqa: PLC0415

        d = dict(src_dict)
        timestamp = datetime.datetime.fromisoformat(d.pop("timestamp"))

        state = SystemStatusResponseState.from_dict(d.pop("state"))

        config = SystemStatusResponseConfig.from_dict(d.pop("config"))

        celery = SystemStatusResponseCelery.from_dict(d.pop("celery"))

        integrations = SystemStatusResponseIntegrations.from_dict(d.pop("integrations"))

        uptime = SystemStatusResponseUptime.from_dict(d.pop("uptime"))

        system_status_response = cls(
            timestamp=timestamp,
            state=state,
            config=config,
            celery=celery,
            integrations=integrations,
            uptime=uptime,
        )

        system_status_response.additional_properties = d
        return system_status_response

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
