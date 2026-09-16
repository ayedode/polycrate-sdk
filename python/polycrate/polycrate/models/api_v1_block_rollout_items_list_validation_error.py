from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.validation_error_enum import ValidationErrorEnum, check_validation_error_enum

if TYPE_CHECKING:
    from ..models.api_v1_block_rollout_items_list_block_error_component import (
        ApiV1BlockRolloutItemsListBlockErrorComponent,
    )
    from ..models.api_v1_block_rollout_items_list_created_by_users_error_component import (
        ApiV1BlockRolloutItemsListCreatedByUsersErrorComponent,
    )
    from ..models.api_v1_block_rollout_items_list_kind_error_component import (
        ApiV1BlockRolloutItemsListKindErrorComponent,
    )
    from ..models.api_v1_block_rollout_items_list_name_exact_error_component import (
        ApiV1BlockRolloutItemsListNameExactErrorComponent,
    )
    from ..models.api_v1_block_rollout_items_list_rollout_error_component import (
        ApiV1BlockRolloutItemsListRolloutErrorComponent,
    )
    from ..models.api_v1_block_rollout_items_list_search_error_component import (
        ApiV1BlockRolloutItemsListSearchErrorComponent,
    )
    from ..models.api_v1_block_rollout_items_list_source_error_component import (
        ApiV1BlockRolloutItemsListSourceErrorComponent,
    )
    from ..models.api_v1_block_rollout_items_list_state_error_component import (
        ApiV1BlockRolloutItemsListStateErrorComponent,
    )
    from ..models.api_v1_block_rollout_items_list_state_not_error_component import (
        ApiV1BlockRolloutItemsListStateNotErrorComponent,
    )
    from ..models.api_v1_block_rollout_items_list_status_error_component import (
        ApiV1BlockRolloutItemsListStatusErrorComponent,
    )
    from ..models.api_v1_block_rollout_items_list_time_range_error_component import (
        ApiV1BlockRolloutItemsListTimeRangeErrorComponent,
    )


T = TypeVar("T", bound="ApiV1BlockRolloutItemsListValidationError")


@_attrs_define
class ApiV1BlockRolloutItemsListValidationError:
    """
    Attributes:
        type_ (ValidationErrorEnum): * `validation_error` - Validation Error
        errors (list[ApiV1BlockRolloutItemsListBlockErrorComponent |
            ApiV1BlockRolloutItemsListCreatedByUsersErrorComponent | ApiV1BlockRolloutItemsListKindErrorComponent |
            ApiV1BlockRolloutItemsListNameExactErrorComponent | ApiV1BlockRolloutItemsListRolloutErrorComponent |
            ApiV1BlockRolloutItemsListSearchErrorComponent | ApiV1BlockRolloutItemsListSourceErrorComponent |
            ApiV1BlockRolloutItemsListStateErrorComponent | ApiV1BlockRolloutItemsListStateNotErrorComponent |
            ApiV1BlockRolloutItemsListStatusErrorComponent | ApiV1BlockRolloutItemsListTimeRangeErrorComponent]):
    """

    type_: ValidationErrorEnum
    errors: list[
        ApiV1BlockRolloutItemsListBlockErrorComponent
        | ApiV1BlockRolloutItemsListCreatedByUsersErrorComponent
        | ApiV1BlockRolloutItemsListKindErrorComponent
        | ApiV1BlockRolloutItemsListNameExactErrorComponent
        | ApiV1BlockRolloutItemsListRolloutErrorComponent
        | ApiV1BlockRolloutItemsListSearchErrorComponent
        | ApiV1BlockRolloutItemsListSourceErrorComponent
        | ApiV1BlockRolloutItemsListStateErrorComponent
        | ApiV1BlockRolloutItemsListStateNotErrorComponent
        | ApiV1BlockRolloutItemsListStatusErrorComponent
        | ApiV1BlockRolloutItemsListTimeRangeErrorComponent
    ]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.api_v1_block_rollout_items_list_block_error_component import (
            ApiV1BlockRolloutItemsListBlockErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollout_items_list_created_by_users_error_component import (
            ApiV1BlockRolloutItemsListCreatedByUsersErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollout_items_list_kind_error_component import (
            ApiV1BlockRolloutItemsListKindErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollout_items_list_rollout_error_component import (
            ApiV1BlockRolloutItemsListRolloutErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollout_items_list_search_error_component import (
            ApiV1BlockRolloutItemsListSearchErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollout_items_list_source_error_component import (
            ApiV1BlockRolloutItemsListSourceErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollout_items_list_state_error_component import (
            ApiV1BlockRolloutItemsListStateErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollout_items_list_state_not_error_component import (
            ApiV1BlockRolloutItemsListStateNotErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollout_items_list_status_error_component import (
            ApiV1BlockRolloutItemsListStatusErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollout_items_list_time_range_error_component import (
            ApiV1BlockRolloutItemsListTimeRangeErrorComponent,  # noqa: PLC0415
        )

        type_: str = self.type_

        errors = []
        for errors_item_data in self.errors:
            errors_item: dict[str, Any]
            if isinstance(errors_item_data, ApiV1BlockRolloutItemsListSearchErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlockRolloutItemsListTimeRangeErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlockRolloutItemsListStateErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlockRolloutItemsListKindErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlockRolloutItemsListCreatedByUsersErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlockRolloutItemsListStatusErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlockRolloutItemsListSourceErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlockRolloutItemsListRolloutErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlockRolloutItemsListBlockErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlockRolloutItemsListStateNotErrorComponent):
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
        from ..models.api_v1_block_rollout_items_list_block_error_component import (
            ApiV1BlockRolloutItemsListBlockErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollout_items_list_created_by_users_error_component import (
            ApiV1BlockRolloutItemsListCreatedByUsersErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollout_items_list_kind_error_component import (
            ApiV1BlockRolloutItemsListKindErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollout_items_list_name_exact_error_component import (
            ApiV1BlockRolloutItemsListNameExactErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollout_items_list_rollout_error_component import (
            ApiV1BlockRolloutItemsListRolloutErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollout_items_list_search_error_component import (
            ApiV1BlockRolloutItemsListSearchErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollout_items_list_source_error_component import (
            ApiV1BlockRolloutItemsListSourceErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollout_items_list_state_error_component import (
            ApiV1BlockRolloutItemsListStateErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollout_items_list_state_not_error_component import (
            ApiV1BlockRolloutItemsListStateNotErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollout_items_list_status_error_component import (
            ApiV1BlockRolloutItemsListStatusErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollout_items_list_time_range_error_component import (
            ApiV1BlockRolloutItemsListTimeRangeErrorComponent,  # noqa: PLC0415
        )

        d = dict(src_dict)
        type_ = check_validation_error_enum(d.pop("type"))

        errors = []
        _errors = d.pop("errors")
        for errors_item_data in _errors:

            def _parse_errors_item(
                data: object,
            ) -> (
                ApiV1BlockRolloutItemsListBlockErrorComponent
                | ApiV1BlockRolloutItemsListCreatedByUsersErrorComponent
                | ApiV1BlockRolloutItemsListKindErrorComponent
                | ApiV1BlockRolloutItemsListNameExactErrorComponent
                | ApiV1BlockRolloutItemsListRolloutErrorComponent
                | ApiV1BlockRolloutItemsListSearchErrorComponent
                | ApiV1BlockRolloutItemsListSourceErrorComponent
                | ApiV1BlockRolloutItemsListStateErrorComponent
                | ApiV1BlockRolloutItemsListStateNotErrorComponent
                | ApiV1BlockRolloutItemsListStatusErrorComponent
                | ApiV1BlockRolloutItemsListTimeRangeErrorComponent
            ):
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_block_rollout_items_list_error_type_0 = (
                        ApiV1BlockRolloutItemsListSearchErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_block_rollout_items_list_error_type_0
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_block_rollout_items_list_error_type_1 = (
                        ApiV1BlockRolloutItemsListTimeRangeErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_block_rollout_items_list_error_type_1
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_block_rollout_items_list_error_type_2 = (
                        ApiV1BlockRolloutItemsListStateErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_block_rollout_items_list_error_type_2
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_block_rollout_items_list_error_type_3 = (
                        ApiV1BlockRolloutItemsListKindErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_block_rollout_items_list_error_type_3
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_block_rollout_items_list_error_type_4 = (
                        ApiV1BlockRolloutItemsListCreatedByUsersErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_block_rollout_items_list_error_type_4
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_block_rollout_items_list_error_type_5 = (
                        ApiV1BlockRolloutItemsListStatusErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_block_rollout_items_list_error_type_5
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_block_rollout_items_list_error_type_6 = (
                        ApiV1BlockRolloutItemsListSourceErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_block_rollout_items_list_error_type_6
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_block_rollout_items_list_error_type_7 = (
                        ApiV1BlockRolloutItemsListRolloutErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_block_rollout_items_list_error_type_7
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_block_rollout_items_list_error_type_8 = (
                        ApiV1BlockRolloutItemsListBlockErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_block_rollout_items_list_error_type_8
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_block_rollout_items_list_error_type_9 = (
                        ApiV1BlockRolloutItemsListStateNotErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_block_rollout_items_list_error_type_9
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_api_v1_block_rollout_items_list_error_type_10 = (
                    ApiV1BlockRolloutItemsListNameExactErrorComponent.from_dict(data)
                )

                return componentsschemas_api_v1_block_rollout_items_list_error_type_10

            errors_item = _parse_errors_item(errors_item_data)

            errors.append(errors_item)

        api_v1_block_rollout_items_list_validation_error = cls(
            type_=type_,
            errors=errors,
        )

        api_v1_block_rollout_items_list_validation_error.additional_properties = d
        return api_v1_block_rollout_items_list_validation_error

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
