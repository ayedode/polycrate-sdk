from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.conversation_kind_enum import ConversationKindEnum, check_conversation_kind_enum
from ..models.conversation_status_enum import ConversationStatusEnum, check_conversation_status_enum
from ..types import UNSET, Unset

T = TypeVar("T", bound="ConversationPost")


@_attrs_define
class ConversationPost:
    """Serializer for Conversation creation.
    Following S3 pattern with validation and create logic.

        Attributes:
            id (UUID):
            name (str):
            kind (ConversationKindEnum | Unset): * `generic` - Generic
                * `zammad` - Zammad
                * `slack` - Slack
                * `discord` - Discord
                * `telegram` - Telegram
                * `msteams` - Microsoft Teams
                * `email` - Email
            status (ConversationStatusEnum | Unset): * `closed` - Closed
                * `waiting_for_operator` - Waiting for Operator
                * `waiting_for_user` - Waiting for User
                * `deleted` - Deleted
            platform_service (bool | Unset): Makes this conversation available for the whole platform
            provider_id (None | str | Unset):
            organization (None | Unset | UUID): Organization that owns this conversation
            conversation_provider (None | Unset | UUID): Provider that manages this conversation
            meta (Any | Unset): Conversation metadata as JSON object
            config (Any | Unset): Conversation configuration as JSON object
    """

    id: UUID
    name: str
    kind: ConversationKindEnum | Unset = UNSET
    status: ConversationStatusEnum | Unset = UNSET
    platform_service: bool | Unset = UNSET
    provider_id: None | str | Unset = UNSET
    organization: None | Unset | UUID = UNSET
    conversation_provider: None | Unset | UUID = UNSET
    meta: Any | Unset = UNSET
    config: Any | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = str(self.id)

        name = self.name

        kind: str | Unset = UNSET
        if not isinstance(self.kind, Unset):
            kind = self.kind

        status: str | Unset = UNSET
        if not isinstance(self.status, Unset):
            status = self.status

        platform_service = self.platform_service

        provider_id: None | str | Unset
        if isinstance(self.provider_id, Unset):
            provider_id = UNSET
        else:
            provider_id = self.provider_id

        organization: None | str | Unset
        if isinstance(self.organization, Unset):
            organization = UNSET
        elif isinstance(self.organization, UUID):
            organization = str(self.organization)
        else:
            organization = self.organization

        conversation_provider: None | str | Unset
        if isinstance(self.conversation_provider, Unset):
            conversation_provider = UNSET
        elif isinstance(self.conversation_provider, UUID):
            conversation_provider = str(self.conversation_provider)
        else:
            conversation_provider = self.conversation_provider

        meta = self.meta

        config = self.config

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "name": name,
            }
        )
        if kind is not UNSET:
            field_dict["kind"] = kind
        if status is not UNSET:
            field_dict["status"] = status
        if platform_service is not UNSET:
            field_dict["platform_service"] = platform_service
        if provider_id is not UNSET:
            field_dict["provider_id"] = provider_id
        if organization is not UNSET:
            field_dict["organization"] = organization
        if conversation_provider is not UNSET:
            field_dict["conversation_provider"] = conversation_provider
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

        _kind = d.pop("kind", UNSET)
        kind: ConversationKindEnum | Unset
        if isinstance(_kind, Unset):
            kind = UNSET
        else:
            kind = check_conversation_kind_enum(_kind)

        _status = d.pop("status", UNSET)
        status: ConversationStatusEnum | Unset
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = check_conversation_status_enum(_status)

        platform_service = d.pop("platform_service", UNSET)

        def _parse_provider_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        provider_id = _parse_provider_id(d.pop("provider_id", UNSET))

        def _parse_organization(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                organization_type_0 = UUID(data)

                return organization_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        organization = _parse_organization(d.pop("organization", UNSET))

        def _parse_conversation_provider(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                conversation_provider_type_0 = UUID(data)

                return conversation_provider_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        conversation_provider = _parse_conversation_provider(d.pop("conversation_provider", UNSET))

        meta = d.pop("meta", UNSET)

        config = d.pop("config", UNSET)

        conversation_post = cls(
            id=id,
            name=name,
            kind=kind,
            status=status,
            platform_service=platform_service,
            provider_id=provider_id,
            organization=organization,
            conversation_provider=conversation_provider,
            meta=meta,
            config=config,
        )

        conversation_post.additional_properties = d
        return conversation_post

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
