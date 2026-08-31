from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.validation_error_enum import ValidationErrorEnum, check_validation_error_enum

if TYPE_CHECKING:
    from ..models.api_v1_block_rollouts_list_created_by_users_error_component import (
        ApiV1BlockRolloutsListCreatedByUsersErrorComponent,
    )
    from ..models.api_v1_block_rollouts_list_kind_error_component import ApiV1BlockRolloutsListKindErrorComponent
    from ..models.api_v1_block_rollouts_list_name_exact_error_component import (
        ApiV1BlockRolloutsListNameExactErrorComponent,
    )
    from ..models.api_v1_block_rollouts_list_rollout_config_error_component import (
        ApiV1BlockRolloutsListRolloutConfigErrorComponent,
    )
    from ..models.api_v1_block_rollouts_list_search_error_component import ApiV1BlockRolloutsListSearchErrorComponent
    from ..models.api_v1_block_rollouts_list_state_error_component import ApiV1BlockRolloutsListStateErrorComponent
    from ..models.api_v1_block_rollouts_list_state_not_error_component import (
        ApiV1BlockRolloutsListStateNotErrorComponent,
    )
    from ..models.api_v1_block_rollouts_list_status_error_component import ApiV1BlockRolloutsListStatusErrorComponent
    from ..models.api_v1_block_rollouts_list_time_range_error_component import (
        ApiV1BlockRolloutsListTimeRangeErrorComponent,
    )


T = TypeVar("T", bound="ApiV1BlockRolloutsListValidationError")


@_attrs_define
class ApiV1BlockRolloutsListValidationError:
    """
    Attributes:
        type_ (ValidationErrorEnum): * `validation_error` - Validation Error
        errors (list[ApiV1BlockRolloutsListCreatedByUsersErrorComponent | ApiV1BlockRolloutsListKindErrorComponent |
            ApiV1BlockRolloutsListNameExactErrorComponent | ApiV1BlockRolloutsListRolloutConfigErrorComponent |
            ApiV1BlockRolloutsListSearchErrorComponent | ApiV1BlockRolloutsListStateErrorComponent |
            ApiV1BlockRolloutsListStateNotErrorComponent | ApiV1BlockRolloutsListStatusErrorComponent |
            ApiV1BlockRolloutsListTimeRangeErrorComponent]):
    """

    type_: ValidationErrorEnum
    errors: list[
        ApiV1BlockRolloutsListCreatedByUsersErrorComponent
        | ApiV1BlockRolloutsListKindErrorComponent
        | ApiV1BlockRolloutsListNameExactErrorComponent
        | ApiV1BlockRolloutsListRolloutConfigErrorComponent
        | ApiV1BlockRolloutsListSearchErrorComponent
        | ApiV1BlockRolloutsListStateErrorComponent
        | ApiV1BlockRolloutsListStateNotErrorComponent
        | ApiV1BlockRolloutsListStatusErrorComponent
        | ApiV1BlockRolloutsListTimeRangeErrorComponent
    ]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.api_v1_block_rollouts_list_created_by_users_error_component import (
            ApiV1BlockRolloutsListCreatedByUsersErrorComponent,
        )
        from ..models.api_v1_block_rollouts_list_kind_error_component import ApiV1BlockRolloutsListKindErrorComponent
        from ..models.api_v1_block_rollouts_list_rollout_config_error_component import (
            ApiV1BlockRolloutsListRolloutConfigErrorComponent,
        )
        from ..models.api_v1_block_rollouts_list_search_error_component import (
            ApiV1BlockRolloutsListSearchErrorComponent,
        )
        from ..models.api_v1_block_rollouts_list_state_error_component import ApiV1BlockRolloutsListStateErrorComponent
        from ..models.api_v1_block_rollouts_list_state_not_error_component import (
            ApiV1BlockRolloutsListStateNotErrorComponent,
        )
        from ..models.api_v1_block_rollouts_list_status_error_component import (
            ApiV1BlockRolloutsListStatusErrorComponent,
        )
        from ..models.api_v1_block_rollouts_list_time_range_error_component import (
            ApiV1BlockRolloutsListTimeRangeErrorComponent,
        )

        type_: str = self.type_

        errors = []
        for errors_item_data in self.errors:
            errors_item: dict[str, Any]
            if isinstance(errors_item_data, ApiV1BlockRolloutsListSearchErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlockRolloutsListTimeRangeErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlockRolloutsListStateErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlockRolloutsListKindErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlockRolloutsListCreatedByUsersErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlockRolloutsListStatusErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlockRolloutsListRolloutConfigErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlockRolloutsListStateNotErrorComponent):
                errors_item = errors_item_data.to_dict()
            else:
                errors_item = errors_item_data.to_dict()

            errors.append(errors_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type_,
                "errors": errors,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.api_v1_block_rollouts_list_created_by_users_error_component import (
            ApiV1BlockRolloutsListCreatedByUsersErrorComponent,
        )
        from ..models.api_v1_block_rollouts_list_kind_error_component import ApiV1BlockRolloutsListKindErrorComponent
        from ..models.api_v1_block_rollouts_list_name_exact_error_component import (
            ApiV1BlockRolloutsListNameExactErrorComponent,
        )
        from ..models.api_v1_block_rollouts_list_rollout_config_error_component import (
            ApiV1BlockRolloutsListRolloutConfigErrorComponent,
        )
        from ..models.api_v1_block_rollouts_list_search_error_component import (
            ApiV1BlockRolloutsListSearchErrorComponent,
        )
        from ..models.api_v1_block_rollouts_list_state_error_component import ApiV1BlockRolloutsListStateErrorComponent
        from ..models.api_v1_block_rollouts_list_state_not_error_component import (
            ApiV1BlockRolloutsListStateNotErrorComponent,
        )
        from ..models.api_v1_block_rollouts_list_status_error_component import (
            ApiV1BlockRolloutsListStatusErrorComponent,
        )
        from ..models.api_v1_block_rollouts_list_time_range_error_component import (
            ApiV1BlockRolloutsListTimeRangeErrorComponent,
        )

        d = dict(src_dict)
        type_ = check_validation_error_enum(d.pop("type"))

        errors = []
        _errors = d.pop("errors")
        for errors_item_data in _errors:

            def _parse_errors_item(
                data: object,
            ) -> (
                ApiV1BlockRolloutsListCreatedByUsersErrorComponent
                | ApiV1BlockRolloutsListKindErrorComponent
                | ApiV1BlockRolloutsListNameExactErrorComponent
                | ApiV1BlockRolloutsListRolloutConfigErrorComponent
                | ApiV1BlockRolloutsListSearchErrorComponent
                | ApiV1BlockRolloutsListStateErrorComponent
                | ApiV1BlockRolloutsListStateNotErrorComponent
                | ApiV1BlockRolloutsListStatusErrorComponent
                | ApiV1BlockRolloutsListTimeRangeErrorComponent
            ):
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_block_rollouts_list_error_type_0 = (
                        ApiV1BlockRolloutsListSearchErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_block_rollouts_list_error_type_0
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_block_rollouts_list_error_type_1 = (
                        ApiV1BlockRolloutsListTimeRangeErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_block_rollouts_list_error_type_1
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_block_rollouts_list_error_type_2 = (
                        ApiV1BlockRolloutsListStateErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_block_rollouts_list_error_type_2
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_block_rollouts_list_error_type_3 = (
                        ApiV1BlockRolloutsListKindErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_block_rollouts_list_error_type_3
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_block_rollouts_list_error_type_4 = (
                        ApiV1BlockRolloutsListCreatedByUsersErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_block_rollouts_list_error_type_4
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_block_rollouts_list_error_type_5 = (
                        ApiV1BlockRolloutsListStatusErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_block_rollouts_list_error_type_5
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_block_rollouts_list_error_type_6 = (
                        ApiV1BlockRolloutsListRolloutConfigErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_block_rollouts_list_error_type_6
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_block_rollouts_list_error_type_7 = (
                        ApiV1BlockRolloutsListStateNotErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_block_rollouts_list_error_type_7
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_api_v1_block_rollouts_list_error_type_8 = (
                    ApiV1BlockRolloutsListNameExactErrorComponent.from_dict(data)
                )

                return componentsschemas_api_v1_block_rollouts_list_error_type_8

            errors_item = _parse_errors_item(errors_item_data)

            errors.append(errors_item)

        api_v1_block_rollouts_list_validation_error = cls(
            type_=type_,
            errors=errors,
        )

        api_v1_block_rollouts_list_validation_error.additional_properties = d
        return api_v1_block_rollouts_list_validation_error

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
