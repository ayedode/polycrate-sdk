from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from .. import types
from ..types import UNSET, Unset

T = TypeVar("T", bound="BlockPromoteAddonSubscriptionRequestRequest")


@_attrs_define
class BlockPromoteAddonSubscriptionRequestRequest:
    """
    Attributes:
        addon (UUID):
        k8s_cluster (UUID | Unset):
    """

    addon: UUID
    k8s_cluster: UUID | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        addon = str(self.addon)

        k8s_cluster: str | Unset = UNSET
        if not isinstance(self.k8s_cluster, Unset):
            k8s_cluster = str(self.k8s_cluster)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "addon": addon,
            }
        )
        if k8s_cluster is not UNSET:
            field_dict["k8s_cluster"] = k8s_cluster

        return field_dict

    def to_multipart(self) -> types.RequestFiles:
        files: types.RequestFiles = []

        files.append(("addon", (None, str(self.addon), "text/plain")))

        if not isinstance(self.k8s_cluster, Unset):
            files.append(("k8s_cluster", (None, str(self.k8s_cluster), "text/plain")))

        for prop_name, prop in self.additional_properties.items():
            files.append((prop_name, (None, str(prop).encode(), "text/plain")))

        return files

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        addon = UUID(d.pop("addon"))

        _k8s_cluster = d.pop("k8s_cluster", UNSET)
        k8s_cluster: UUID | Unset
        if isinstance(_k8s_cluster, Unset):
            k8s_cluster = UNSET
        else:
            k8s_cluster = UUID(_k8s_cluster)

        block_promote_addon_subscription_request_request = cls(
            addon=addon,
            k8s_cluster=k8s_cluster,
        )

        block_promote_addon_subscription_request_request.additional_properties = d
        return block_promote_addon_subscription_request_request

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
