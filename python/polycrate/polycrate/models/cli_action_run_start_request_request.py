from __future__ import annotations

import json
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from .. import types
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.cli_action_run_start_request_request_block_config_type_0 import (
        CLIActionRunStartRequestRequestBlockConfigType0,
    )
    from ..models.cli_action_run_start_request_request_block_labels_type_0 import (
        CLIActionRunStartRequestRequestBlockLabelsType0,
    )


T = TypeVar("T", bound="CLIActionRunStartRequestRequest")


@_attrs_define
class CLIActionRunStartRequestRequest:
    """
    Attributes:
        organization (str): Organization name
        workspace (str): Workspace name
        block (str): Block name
        action (str): Action name
        started_at (str | Unset): ISO 8601 start timestamp
        block_config (CLIActionRunStartRequestRequestBlockConfigType0 | None | Unset): Block config snapshot
        block_labels (CLIActionRunStartRequestRequestBlockLabelsType0 | None | Unset): Block labels snapshot
        block_version (str | Unset): Block version
        force (bool | Unset): Cancel conflicting ActionRun and proceed Default: False.
    """

    organization: str
    workspace: str
    block: str
    action: str
    started_at: str | Unset = UNSET
    block_config: CLIActionRunStartRequestRequestBlockConfigType0 | None | Unset = UNSET
    block_labels: CLIActionRunStartRequestRequestBlockLabelsType0 | None | Unset = UNSET
    block_version: str | Unset = UNSET
    force: bool | Unset = False
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.cli_action_run_start_request_request_block_config_type_0 import (
            CLIActionRunStartRequestRequestBlockConfigType0,
        )
        from ..models.cli_action_run_start_request_request_block_labels_type_0 import (
            CLIActionRunStartRequestRequestBlockLabelsType0,
        )

        organization = self.organization

        workspace = self.workspace

        block = self.block

        action = self.action

        started_at = self.started_at

        block_config: dict[str, Any] | None | Unset
        if isinstance(self.block_config, Unset):
            block_config = UNSET
        elif isinstance(self.block_config, CLIActionRunStartRequestRequestBlockConfigType0):
            block_config = self.block_config.to_dict()
        else:
            block_config = self.block_config

        block_labels: dict[str, Any] | None | Unset
        if isinstance(self.block_labels, Unset):
            block_labels = UNSET
        elif isinstance(self.block_labels, CLIActionRunStartRequestRequestBlockLabelsType0):
            block_labels = self.block_labels.to_dict()
        else:
            block_labels = self.block_labels

        block_version = self.block_version

        force = self.force

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "organization": organization,
                "workspace": workspace,
                "block": block,
                "action": action,
            }
        )
        if started_at is not UNSET:
            field_dict["started_at"] = started_at
        if block_config is not UNSET:
            field_dict["block_config"] = block_config
        if block_labels is not UNSET:
            field_dict["block_labels"] = block_labels
        if block_version is not UNSET:
            field_dict["block_version"] = block_version
        if force is not UNSET:
            field_dict["force"] = force

        return field_dict

    def to_multipart(self) -> types.RequestFiles:
        from ..models.cli_action_run_start_request_request_block_config_type_0 import (
            CLIActionRunStartRequestRequestBlockConfigType0,
        )
        from ..models.cli_action_run_start_request_request_block_labels_type_0 import (
            CLIActionRunStartRequestRequestBlockLabelsType0,
        )

        files: types.RequestFiles = []

        files.append(("organization", (None, str(self.organization).encode(), "text/plain")))

        files.append(("workspace", (None, str(self.workspace).encode(), "text/plain")))

        files.append(("block", (None, str(self.block).encode(), "text/plain")))

        files.append(("action", (None, str(self.action).encode(), "text/plain")))

        if not isinstance(self.started_at, Unset):
            files.append(("started_at", (None, str(self.started_at).encode(), "text/plain")))

        if not isinstance(self.block_config, Unset):
            if isinstance(self.block_config, CLIActionRunStartRequestRequestBlockConfigType0):
                files.append(
                    ("block_config", (None, json.dumps(self.block_config.to_dict()).encode(), "application/json"))
                )
            else:
                files.append(("block_config", (None, str(self.block_config).encode(), "text/plain")))

        if not isinstance(self.block_labels, Unset):
            if isinstance(self.block_labels, CLIActionRunStartRequestRequestBlockLabelsType0):
                files.append(
                    ("block_labels", (None, json.dumps(self.block_labels.to_dict()).encode(), "application/json"))
                )
            else:
                files.append(("block_labels", (None, str(self.block_labels).encode(), "text/plain")))

        if not isinstance(self.block_version, Unset):
            files.append(("block_version", (None, str(self.block_version).encode(), "text/plain")))

        if not isinstance(self.force, Unset):
            files.append(("force", (None, str(self.force).encode(), "text/plain")))

        for prop_name, prop in self.additional_properties.items():
            files.append((prop_name, (None, str(prop).encode(), "text/plain")))

        return files

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.cli_action_run_start_request_request_block_config_type_0 import (
            CLIActionRunStartRequestRequestBlockConfigType0,
        )
        from ..models.cli_action_run_start_request_request_block_labels_type_0 import (
            CLIActionRunStartRequestRequestBlockLabelsType0,
        )

        d = dict(src_dict)
        organization = d.pop("organization")

        workspace = d.pop("workspace")

        block = d.pop("block")

        action = d.pop("action")

        started_at = d.pop("started_at", UNSET)

        def _parse_block_config(data: object) -> CLIActionRunStartRequestRequestBlockConfigType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                block_config_type_0 = CLIActionRunStartRequestRequestBlockConfigType0.from_dict(data)

                return block_config_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(CLIActionRunStartRequestRequestBlockConfigType0 | None | Unset, data)

        block_config = _parse_block_config(d.pop("block_config", UNSET))

        def _parse_block_labels(data: object) -> CLIActionRunStartRequestRequestBlockLabelsType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                block_labels_type_0 = CLIActionRunStartRequestRequestBlockLabelsType0.from_dict(data)

                return block_labels_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(CLIActionRunStartRequestRequestBlockLabelsType0 | None | Unset, data)

        block_labels = _parse_block_labels(d.pop("block_labels", UNSET))

        block_version = d.pop("block_version", UNSET)

        force = d.pop("force", UNSET)

        cli_action_run_start_request_request = cls(
            organization=organization,
            workspace=workspace,
            block=block,
            action=action,
            started_at=started_at,
            block_config=block_config,
            block_labels=block_labels,
            block_version=block_version,
            force=force,
        )

        cli_action_run_start_request_request.additional_properties = d
        return cli_action_run_start_request_request

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
