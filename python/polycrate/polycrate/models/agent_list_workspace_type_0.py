from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.agent_list_workspace_type_0_created_by_type_0 import AgentListWorkspaceType0CreatedByType0


T = TypeVar("T", bound="AgentListWorkspaceType0")


@_attrs_define
class AgentListWorkspaceType0:
    """
    Attributes:
        id (UUID | Unset):
        name (str | Unset):
        display_name (None | str | Unset):
        slug (None | str | Unset):
        kind (None | str | Unset):
        reconciliation_running (bool | None | Unset):
        created_at (datetime.datetime | None | Unset):
        created_by (AgentListWorkspaceType0CreatedByType0 | None | Unset):
        url (None | str | Unset):
    """

    id: UUID | Unset = UNSET
    name: str | Unset = UNSET
    display_name: None | str | Unset = UNSET
    slug: None | str | Unset = UNSET
    kind: None | str | Unset = UNSET
    reconciliation_running: bool | None | Unset = UNSET
    created_at: datetime.datetime | None | Unset = UNSET
    created_by: AgentListWorkspaceType0CreatedByType0 | None | Unset = UNSET
    url: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.agent_list_workspace_type_0_created_by_type_0 import (
            AgentListWorkspaceType0CreatedByType0,  # noqa: PLC0415
        )

        id: str | Unset = UNSET
        if not isinstance(self.id, Unset):
            id = str(self.id)

        name = self.name

        display_name: None | str | Unset
        if isinstance(self.display_name, Unset):
            display_name = UNSET
        else:
            display_name = self.display_name

        slug: None | str | Unset
        if isinstance(self.slug, Unset):
            slug = UNSET
        else:
            slug = self.slug

        kind: None | str | Unset
        if isinstance(self.kind, Unset):
            kind = UNSET
        else:
            kind = self.kind

        reconciliation_running: bool | None | Unset
        if isinstance(self.reconciliation_running, Unset):
            reconciliation_running = UNSET
        else:
            reconciliation_running = self.reconciliation_running

        created_at: None | str | Unset
        if isinstance(self.created_at, Unset):
            created_at = UNSET
        elif isinstance(self.created_at, datetime.datetime):
            created_at = self.created_at.isoformat()
        else:
            created_at = self.created_at

        created_by: dict[str, Any] | None | Unset
        if isinstance(self.created_by, Unset):
            created_by = UNSET
        elif isinstance(self.created_by, AgentListWorkspaceType0CreatedByType0):
            created_by = self.created_by.to_dict()
        else:
            created_by = self.created_by

        url: None | str | Unset
        if isinstance(self.url, Unset):
            url = UNSET
        else:
            url = self.url

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if name is not UNSET:
            field_dict["name"] = name
        if display_name is not UNSET:
            field_dict["display_name"] = display_name
        if slug is not UNSET:
            field_dict["slug"] = slug
        if kind is not UNSET:
            field_dict["kind"] = kind
        if reconciliation_running is not UNSET:
            field_dict["reconciliation_running"] = reconciliation_running
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if created_by is not UNSET:
            field_dict["created_by"] = created_by
        if url is not UNSET:
            field_dict["url"] = url

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.agent_list_workspace_type_0_created_by_type_0 import (
            AgentListWorkspaceType0CreatedByType0,  # noqa: PLC0415
        )

        d = dict(src_dict)
        _id = d.pop("id", UNSET)
        id: UUID | Unset
        if isinstance(_id, Unset):
            id = UNSET
        else:
            id = UUID(_id)

        name = d.pop("name", UNSET)

        def _parse_display_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        display_name = _parse_display_name(d.pop("display_name", UNSET))

        def _parse_slug(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        slug = _parse_slug(d.pop("slug", UNSET))

        def _parse_kind(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        kind = _parse_kind(d.pop("kind", UNSET))

        def _parse_reconciliation_running(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        reconciliation_running = _parse_reconciliation_running(d.pop("reconciliation_running", UNSET))

        def _parse_created_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                created_at_type_0 = datetime.datetime.fromisoformat(data)

                return created_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        created_at = _parse_created_at(d.pop("created_at", UNSET))

        def _parse_created_by(data: object) -> AgentListWorkspaceType0CreatedByType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                created_by_type_0 = AgentListWorkspaceType0CreatedByType0.from_dict(data)

                return created_by_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(AgentListWorkspaceType0CreatedByType0 | None | Unset, data)

        created_by = _parse_created_by(d.pop("created_by", UNSET))

        def _parse_url(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        url = _parse_url(d.pop("url", UNSET))

        agent_list_workspace_type_0 = cls(
            id=id,
            name=name,
            display_name=display_name,
            slug=slug,
            kind=kind,
            reconciliation_running=reconciliation_running,
            created_at=created_at,
            created_by=created_by,
            url=url,
        )

        agent_list_workspace_type_0.additional_properties = d
        return agent_list_workspace_type_0

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
