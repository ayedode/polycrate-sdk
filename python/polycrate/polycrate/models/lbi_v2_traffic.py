from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.lbi_v2_retries import LbiV2Retries
    from ..models.lbi_v2_session_affinity import LbiV2SessionAffinity
    from ..models.lbi_v2_timeouts import LbiV2Timeouts


T = TypeVar("T", bound="LbiV2Traffic")


@_attrs_define
class LbiV2Traffic:
    """
    Attributes:
        timeouts (LbiV2Timeouts | None | Unset):
        retries (LbiV2Retries | None | Unset):
        session_affinity (LbiV2SessionAffinity | None | Unset):
        proxy_protocol (str | Unset):
        websockets (bool | Unset):
        http2 (bool | Unset):
        http3 (bool | Unset):
    """

    timeouts: LbiV2Timeouts | None | Unset = UNSET
    retries: LbiV2Retries | None | Unset = UNSET
    session_affinity: LbiV2SessionAffinity | None | Unset = UNSET
    proxy_protocol: str | Unset = UNSET
    websockets: bool | Unset = UNSET
    http2: bool | Unset = UNSET
    http3: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.lbi_v2_retries import LbiV2Retries  # noqa: PLC0415
        from ..models.lbi_v2_session_affinity import LbiV2SessionAffinity  # noqa: PLC0415
        from ..models.lbi_v2_timeouts import LbiV2Timeouts  # noqa: PLC0415

        timeouts: dict[str, Any] | None | Unset
        if isinstance(self.timeouts, Unset):
            timeouts = UNSET
        elif isinstance(self.timeouts, LbiV2Timeouts):
            timeouts = self.timeouts.to_dict()
        else:
            timeouts = self.timeouts

        retries: dict[str, Any] | None | Unset
        if isinstance(self.retries, Unset):
            retries = UNSET
        elif isinstance(self.retries, LbiV2Retries):
            retries = self.retries.to_dict()
        else:
            retries = self.retries

        session_affinity: dict[str, Any] | None | Unset
        if isinstance(self.session_affinity, Unset):
            session_affinity = UNSET
        elif isinstance(self.session_affinity, LbiV2SessionAffinity):
            session_affinity = self.session_affinity.to_dict()
        else:
            session_affinity = self.session_affinity

        proxy_protocol = self.proxy_protocol

        websockets = self.websockets

        http2 = self.http2

        http3 = self.http3

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if timeouts is not UNSET:
            field_dict["timeouts"] = timeouts
        if retries is not UNSET:
            field_dict["retries"] = retries
        if session_affinity is not UNSET:
            field_dict["sessionAffinity"] = session_affinity
        if proxy_protocol is not UNSET:
            field_dict["proxyProtocol"] = proxy_protocol
        if websockets is not UNSET:
            field_dict["websockets"] = websockets
        if http2 is not UNSET:
            field_dict["http2"] = http2
        if http3 is not UNSET:
            field_dict["http3"] = http3

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.lbi_v2_retries import LbiV2Retries  # noqa: PLC0415
        from ..models.lbi_v2_session_affinity import LbiV2SessionAffinity  # noqa: PLC0415
        from ..models.lbi_v2_timeouts import LbiV2Timeouts  # noqa: PLC0415

        d = dict(src_dict)

        def _parse_timeouts(data: object) -> LbiV2Timeouts | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                timeouts_type_1 = LbiV2Timeouts.from_dict(data)

                return timeouts_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(LbiV2Timeouts | None | Unset, data)

        timeouts = _parse_timeouts(d.pop("timeouts", UNSET))

        def _parse_retries(data: object) -> LbiV2Retries | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                retries_type_1 = LbiV2Retries.from_dict(data)

                return retries_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(LbiV2Retries | None | Unset, data)

        retries = _parse_retries(d.pop("retries", UNSET))

        def _parse_session_affinity(data: object) -> LbiV2SessionAffinity | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                session_affinity_type_1 = LbiV2SessionAffinity.from_dict(data)

                return session_affinity_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(LbiV2SessionAffinity | None | Unset, data)

        session_affinity = _parse_session_affinity(d.pop("sessionAffinity", UNSET))

        proxy_protocol = d.pop("proxyProtocol", UNSET)

        websockets = d.pop("websockets", UNSET)

        http2 = d.pop("http2", UNSET)

        http3 = d.pop("http3", UNSET)

        lbi_v2_traffic = cls(
            timeouts=timeouts,
            retries=retries,
            session_affinity=session_affinity,
            proxy_protocol=proxy_protocol,
            websockets=websockets,
            http2=http2,
            http3=http3,
        )

        lbi_v2_traffic.additional_properties = d
        return lbi_v2_traffic

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
