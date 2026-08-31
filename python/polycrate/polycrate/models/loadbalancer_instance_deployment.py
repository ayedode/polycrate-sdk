from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.deployment_status_enum import DeploymentStatusEnum, check_deployment_status_enum

if TYPE_CHECKING:
    from ..models.region_simple import RegionSimple


T = TypeVar("T", bound="LoadbalancerInstanceDeployment")


@_attrs_define
class LoadbalancerInstanceDeployment:
    """
    Attributes:
        deployment_status (DeploymentStatusEnum): * `pending` - Pending
            * `deploying` - Deploying
            * `deployed` - Deployed
            * `failed` - Failed
            * `removing` - Removing
        last_deployment_attempt (datetime.datetime | None):
        deployment_error (None | str):
        loadbalancer_region (str):
        region (RegionSimple):
    """

    deployment_status: DeploymentStatusEnum
    last_deployment_attempt: datetime.datetime | None
    deployment_error: None | str
    loadbalancer_region: str
    region: RegionSimple
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        deployment_status: str = self.deployment_status

        last_deployment_attempt: None | str
        if isinstance(self.last_deployment_attempt, datetime.datetime):
            last_deployment_attempt = self.last_deployment_attempt.isoformat()
        else:
            last_deployment_attempt = self.last_deployment_attempt

        deployment_error: None | str
        deployment_error = self.deployment_error

        loadbalancer_region = self.loadbalancer_region

        region = self.region.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "deployment_status": deployment_status,
                "last_deployment_attempt": last_deployment_attempt,
                "deployment_error": deployment_error,
                "loadbalancer_region": loadbalancer_region,
                "region": region,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.region_simple import RegionSimple

        d = dict(src_dict)
        deployment_status = check_deployment_status_enum(d.pop("deployment_status"))

        def _parse_last_deployment_attempt(data: object) -> datetime.datetime | None:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                last_deployment_attempt_type_0 = datetime.datetime.fromisoformat(data)

                return last_deployment_attempt_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None, data)

        last_deployment_attempt = _parse_last_deployment_attempt(d.pop("last_deployment_attempt"))

        def _parse_deployment_error(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        deployment_error = _parse_deployment_error(d.pop("deployment_error"))

        loadbalancer_region = d.pop("loadbalancer_region")

        region = RegionSimple.from_dict(d.pop("region"))

        loadbalancer_instance_deployment = cls(
            deployment_status=deployment_status,
            last_deployment_attempt=last_deployment_attempt,
            deployment_error=deployment_error,
            loadbalancer_region=loadbalancer_region,
            region=region,
        )

        loadbalancer_instance_deployment.additional_properties = d
        return loadbalancer_instance_deployment

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
