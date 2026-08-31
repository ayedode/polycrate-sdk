from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.conversation_status_enum import ConversationStatusEnum, check_conversation_status_enum
from ..types import UNSET, Unset

T = TypeVar("T", bound="ConversationUpdate")


@_attrs_define
class ConversationUpdate:
    """Serializer for Conversation updates.
    Following S3 pattern with restricted update fields.

        Attributes:
            id (UUID):
            name (str):
            organization (None | UUID): Organization that owns this conversation
            conversation_provider (None | UUID): Provider that manages this conversation
            status (ConversationStatusEnum | Unset): * `closed` - Closed
                * `waiting_for_operator` - Waiting for Operator
                * `waiting_for_user` - Waiting for User
                * `deleted` - Deleted
            provider_id (None | str | Unset):
            meta (Any | Unset): Conversation metadata as JSON object
            config (Any | Unset): Conversation configuration as JSON object
    """

    id: UUID
    name: str
    organization: None | UUID
    conversation_provider: None | UUID
    status: ConversationStatusEnum | Unset = UNSET
    provider_id: None | str | Unset = UNSET
    meta: Any | Unset = UNSET
    config: Any | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = str(self.id)

        name = self.name

        organization: None | str
        if isinstance(self.organization, UUID):
            organization = str(self.organization)
        else:
            organization = self.organization

        conversation_provider: None | str
        if isinstance(self.conversation_provider, UUID):
            conversation_provider = str(self.conversation_provider)
        else:
            conversation_provider = self.conversation_provider

        status: str | Unset = UNSET
        if not isinstance(self.status, Unset):
            status = self.status

        provider_id: None | str | Unset
        if isinstance(self.provider_id, Unset):
            provider_id = UNSET
        else:
            provider_id = self.provider_id

        meta = self.meta

        config = self.config

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "name": name,
                "organization": organization,
                "conversation_provider": conversation_provider,
            }
        )
        if status is not UNSET:
            field_dict["status"] = status
        if provider_id is not UNSET:
            field_dict["provider_id"] = provider_id
        if meta is not UNSET:
            field_dict["meta"] = meta
        if config is not UNSET:
            field_dict["config"] = config

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = UUID(d.pop("id"))

        name = d.pop("name")

        def _parse_organization(data: object) -> None | UUID:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                organization_type_0 = UUID(data)

                return organization_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | UUID, data)

        organization = _parse_organization(d.pop("organization"))

        def _parse_conversation_provider(data: object) -> None | UUID:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                conversation_provider_type_0 = UUID(data)

                return conversation_provider_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | UUID, data)

        conversation_provider = _parse_conversation_provider(d.pop("conversation_provider"))

        _status = d.pop("status", UNSET)
        status: ConversationStatusEnum | Unset
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = check_conversation_status_enum(_status)

        def _parse_provider_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        provider_id = _parse_provider_id(d.pop("provider_id", UNSET))

        meta = d.pop("meta", UNSET)

        config = d.pop("config", UNSET)

        conversation_update = cls(
            id=id,
            name=name,
            organization=organization,
            conversation_provider=conversation_provider,
            status=status,
            provider_id=provider_id,
            meta=meta,
            config=config,
        )

        conversation_update.additional_properties = d
        return conversation_update

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
