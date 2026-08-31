from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.validation_error_enum import ValidationErrorEnum, check_validation_error_enum

if TYPE_CHECKING:
    from ..models.api_v1_alertcategories_create_active_error_component import (
        ApiV1AlertcategoriesCreateActiveErrorComponent,
    )
    from ..models.api_v1_alertcategories_create_annotations_error_component import (
        ApiV1AlertcategoriesCreateAnnotationsErrorComponent,
    )
    from ..models.api_v1_alertcategories_create_archived_at_error_component import (
        ApiV1AlertcategoriesCreateArchivedAtErrorComponent,
    )
    from ..models.api_v1_alertcategories_create_archived_error_component import (
        ApiV1AlertcategoriesCreateArchivedErrorComponent,
    )
    from ..models.api_v1_alertcategories_create_archived_reason_error_component import (
        ApiV1AlertcategoriesCreateArchivedReasonErrorComponent,
    )
    from ..models.api_v1_alertcategories_create_criticality_error_component import (
        ApiV1AlertcategoriesCreateCriticalityErrorComponent,
    )
    from ..models.api_v1_alertcategories_create_debug_mode_error_component import (
        ApiV1AlertcategoriesCreateDebugModeErrorComponent,
    )
    from ..models.api_v1_alertcategories_create_description_error_component import (
        ApiV1AlertcategoriesCreateDescriptionErrorComponent,
    )
    from ..models.api_v1_alertcategories_create_display_name_error_component import (
        ApiV1AlertcategoriesCreateDisplayNameErrorComponent,
    )
    from ..models.api_v1_alertcategories_create_kind_error_component import ApiV1AlertcategoriesCreateKindErrorComponent
    from ..models.api_v1_alertcategories_create_labels_error_component import (
        ApiV1AlertcategoriesCreateLabelsErrorComponent,
    )
    from ..models.api_v1_alertcategories_create_name_error_component import ApiV1AlertcategoriesCreateNameErrorComponent
    from ..models.api_v1_alertcategories_create_non_field_errors_error_component import (
        ApiV1AlertcategoriesCreateNonFieldErrorsErrorComponent,
    )
    from ..models.api_v1_alertcategories_create_platform_service_error_component import (
        ApiV1AlertcategoriesCreatePlatformServiceErrorComponent,
    )
    from ..models.api_v1_alertcategories_create_provider_error_component import (
        ApiV1AlertcategoriesCreateProviderErrorComponent,
    )
    from ..models.api_v1_alertcategories_create_provider_id_error_component import (
        ApiV1AlertcategoriesCreateProviderIdErrorComponent,
    )
    from ..models.api_v1_alertcategories_create_provider_reference_error_component import (
        ApiV1AlertcategoriesCreateProviderReferenceErrorComponent,
    )
    from ..models.api_v1_alertcategories_create_reconciliation_enabled_error_component import (
        ApiV1AlertcategoriesCreateReconciliationEnabledErrorComponent,
    )
    from ..models.api_v1_alertcategories_create_sla_availability_error_component import (
        ApiV1AlertcategoriesCreateSlaAvailabilityErrorComponent,
    )
    from ..models.api_v1_alertcategories_create_sla_target_error_component import (
        ApiV1AlertcategoriesCreateSlaTargetErrorComponent,
    )
    from ..models.api_v1_alertcategories_create_slo_availability_error_component import (
        ApiV1AlertcategoriesCreateSloAvailabilityErrorComponent,
    )
    from ..models.api_v1_alertcategories_create_slo_target_error_component import (
        ApiV1AlertcategoriesCreateSloTargetErrorComponent,
    )
    from ..models.api_v1_alertcategories_create_sort_order_error_component import (
        ApiV1AlertcategoriesCreateSortOrderErrorComponent,
    )
    from ..models.api_v1_alertcategories_create_target_availability_error_component import (
        ApiV1AlertcategoriesCreateTargetAvailabilityErrorComponent,
    )
    from ..models.api_v1_alertcategories_create_tolerations_error_component import (
        ApiV1AlertcategoriesCreateTolerationsErrorComponent,
    )


T = TypeVar("T", bound="ApiV1AlertcategoriesCreateValidationError")


@_attrs_define
class ApiV1AlertcategoriesCreateValidationError:
    """
    Attributes:
        type_ (ValidationErrorEnum): * `validation_error` - Validation Error
        errors (list[ApiV1AlertcategoriesCreateActiveErrorComponent |
            ApiV1AlertcategoriesCreateAnnotationsErrorComponent | ApiV1AlertcategoriesCreateArchivedAtErrorComponent |
            ApiV1AlertcategoriesCreateArchivedErrorComponent | ApiV1AlertcategoriesCreateArchivedReasonErrorComponent |
            ApiV1AlertcategoriesCreateCriticalityErrorComponent | ApiV1AlertcategoriesCreateDebugModeErrorComponent |
            ApiV1AlertcategoriesCreateDescriptionErrorComponent | ApiV1AlertcategoriesCreateDisplayNameErrorComponent |
            ApiV1AlertcategoriesCreateKindErrorComponent | ApiV1AlertcategoriesCreateLabelsErrorComponent |
            ApiV1AlertcategoriesCreateNameErrorComponent | ApiV1AlertcategoriesCreateNonFieldErrorsErrorComponent |
            ApiV1AlertcategoriesCreatePlatformServiceErrorComponent | ApiV1AlertcategoriesCreateProviderErrorComponent |
            ApiV1AlertcategoriesCreateProviderIdErrorComponent | ApiV1AlertcategoriesCreateProviderReferenceErrorComponent |
            ApiV1AlertcategoriesCreateReconciliationEnabledErrorComponent |
            ApiV1AlertcategoriesCreateSlaAvailabilityErrorComponent | ApiV1AlertcategoriesCreateSlaTargetErrorComponent |
            ApiV1AlertcategoriesCreateSloAvailabilityErrorComponent | ApiV1AlertcategoriesCreateSloTargetErrorComponent |
            ApiV1AlertcategoriesCreateSortOrderErrorComponent | ApiV1AlertcategoriesCreateTargetAvailabilityErrorComponent |
            ApiV1AlertcategoriesCreateTolerationsErrorComponent]):
    """

    type_: ValidationErrorEnum
    errors: list[
        ApiV1AlertcategoriesCreateActiveErrorComponent
        | ApiV1AlertcategoriesCreateAnnotationsErrorComponent
        | ApiV1AlertcategoriesCreateArchivedAtErrorComponent
        | ApiV1AlertcategoriesCreateArchivedErrorComponent
        | ApiV1AlertcategoriesCreateArchivedReasonErrorComponent
        | ApiV1AlertcategoriesCreateCriticalityErrorComponent
        | ApiV1AlertcategoriesCreateDebugModeErrorComponent
        | ApiV1AlertcategoriesCreateDescriptionErrorComponent
        | ApiV1AlertcategoriesCreateDisplayNameErrorComponent
        | ApiV1AlertcategoriesCreateKindErrorComponent
        | ApiV1AlertcategoriesCreateLabelsErrorComponent
        | ApiV1AlertcategoriesCreateNameErrorComponent
        | ApiV1AlertcategoriesCreateNonFieldErrorsErrorComponent
        | ApiV1AlertcategoriesCreatePlatformServiceErrorComponent
        | ApiV1AlertcategoriesCreateProviderErrorComponent
        | ApiV1AlertcategoriesCreateProviderIdErrorComponent
        | ApiV1AlertcategoriesCreateProviderReferenceErrorComponent
        | ApiV1AlertcategoriesCreateReconciliationEnabledErrorComponent
        | ApiV1AlertcategoriesCreateSlaAvailabilityErrorComponent
        | ApiV1AlertcategoriesCreateSlaTargetErrorComponent
        | ApiV1AlertcategoriesCreateSloAvailabilityErrorComponent
        | ApiV1AlertcategoriesCreateSloTargetErrorComponent
        | ApiV1AlertcategoriesCreateSortOrderErrorComponent
        | ApiV1AlertcategoriesCreateTargetAvailabilityErrorComponent
        | ApiV1AlertcategoriesCreateTolerationsErrorComponent
    ]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.api_v1_alertcategories_create_annotations_error_component import (
            ApiV1AlertcategoriesCreateAnnotationsErrorComponent,
        )
        from ..models.api_v1_alertcategories_create_archived_at_error_component import (
            ApiV1AlertcategoriesCreateArchivedAtErrorComponent,
        )
        from ..models.api_v1_alertcategories_create_archived_error_component import (
            ApiV1AlertcategoriesCreateArchivedErrorComponent,
        )
        from ..models.api_v1_alertcategories_create_archived_reason_error_component import (
            ApiV1AlertcategoriesCreateArchivedReasonErrorComponent,
        )
        from ..models.api_v1_alertcategories_create_criticality_error_component import (
            ApiV1AlertcategoriesCreateCriticalityErrorComponent,
        )
        from ..models.api_v1_alertcategories_create_debug_mode_error_component import (
            ApiV1AlertcategoriesCreateDebugModeErrorComponent,
        )
        from ..models.api_v1_alertcategories_create_description_error_component import (
            ApiV1AlertcategoriesCreateDescriptionErrorComponent,
        )
        from ..models.api_v1_alertcategories_create_display_name_error_component import (
            ApiV1AlertcategoriesCreateDisplayNameErrorComponent,
        )
        from ..models.api_v1_alertcategories_create_kind_error_component import (
            ApiV1AlertcategoriesCreateKindErrorComponent,
        )
        from ..models.api_v1_alertcategories_create_labels_error_component import (
            ApiV1AlertcategoriesCreateLabelsErrorComponent,
        )
        from ..models.api_v1_alertcategories_create_name_error_component import (
            ApiV1AlertcategoriesCreateNameErrorComponent,
        )
        from ..models.api_v1_alertcategories_create_non_field_errors_error_component import (
            ApiV1AlertcategoriesCreateNonFieldErrorsErrorComponent,
        )
        from ..models.api_v1_alertcategories_create_platform_service_error_component import (
            ApiV1AlertcategoriesCreatePlatformServiceErrorComponent,
        )
        from ..models.api_v1_alertcategories_create_provider_error_component import (
            ApiV1AlertcategoriesCreateProviderErrorComponent,
        )
        from ..models.api_v1_alertcategories_create_provider_id_error_component import (
            ApiV1AlertcategoriesCreateProviderIdErrorComponent,
        )
        from ..models.api_v1_alertcategories_create_provider_reference_error_component import (
            ApiV1AlertcategoriesCreateProviderReferenceErrorComponent,
        )
        from ..models.api_v1_alertcategories_create_reconciliation_enabled_error_component import (
            ApiV1AlertcategoriesCreateReconciliationEnabledErrorComponent,
        )
        from ..models.api_v1_alertcategories_create_sla_availability_error_component import (
            ApiV1AlertcategoriesCreateSlaAvailabilityErrorComponent,
        )
        from ..models.api_v1_alertcategories_create_sla_target_error_component import (
            ApiV1AlertcategoriesCreateSlaTargetErrorComponent,
        )
        from ..models.api_v1_alertcategories_create_slo_availability_error_component import (
            ApiV1AlertcategoriesCreateSloAvailabilityErrorComponent,
        )
        from ..models.api_v1_alertcategories_create_slo_target_error_component import (
            ApiV1AlertcategoriesCreateSloTargetErrorComponent,
        )
        from ..models.api_v1_alertcategories_create_sort_order_error_component import (
            ApiV1AlertcategoriesCreateSortOrderErrorComponent,
        )
        from ..models.api_v1_alertcategories_create_target_availability_error_component import (
            ApiV1AlertcategoriesCreateTargetAvailabilityErrorComponent,
        )
        from ..models.api_v1_alertcategories_create_tolerations_error_component import (
            ApiV1AlertcategoriesCreateTolerationsErrorComponent,
        )

        type_: str = self.type_

        errors = []
        for errors_item_data in self.errors:
            errors_item: dict[str, Any]
            if isinstance(errors_item_data, ApiV1AlertcategoriesCreateNonFieldErrorsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1AlertcategoriesCreateNameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1AlertcategoriesCreateDisplayNameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1AlertcategoriesCreateLabelsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1AlertcategoriesCreateAnnotationsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1AlertcategoriesCreateDebugModeErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1AlertcategoriesCreateProviderErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1AlertcategoriesCreateProviderReferenceErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1AlertcategoriesCreateProviderIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1AlertcategoriesCreateReconciliationEnabledErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1AlertcategoriesCreatePlatformServiceErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1AlertcategoriesCreateKindErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1AlertcategoriesCreateTolerationsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1AlertcategoriesCreateArchivedErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1AlertcategoriesCreateArchivedAtErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1AlertcategoriesCreateArchivedReasonErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1AlertcategoriesCreateCriticalityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1AlertcategoriesCreateTargetAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1AlertcategoriesCreateSloTargetErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1AlertcategoriesCreateSloAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1AlertcategoriesCreateSlaTargetErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1AlertcategoriesCreateSlaAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1AlertcategoriesCreateDescriptionErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1AlertcategoriesCreateSortOrderErrorComponent):
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
        from ..models.api_v1_alertcategories_create_active_error_component import (
            ApiV1AlertcategoriesCreateActiveErrorComponent,
        )
        from ..models.api_v1_alertcategories_create_annotations_error_component import (
            ApiV1AlertcategoriesCreateAnnotationsErrorComponent,
        )
        from ..models.api_v1_alertcategories_create_archived_at_error_component import (
            ApiV1AlertcategoriesCreateArchivedAtErrorComponent,
        )
        from ..models.api_v1_alertcategories_create_archived_error_component import (
            ApiV1AlertcategoriesCreateArchivedErrorComponent,
        )
        from ..models.api_v1_alertcategories_create_archived_reason_error_component import (
            ApiV1AlertcategoriesCreateArchivedReasonErrorComponent,
        )
        from ..models.api_v1_alertcategories_create_criticality_error_component import (
            ApiV1AlertcategoriesCreateCriticalityErrorComponent,
        )
        from ..models.api_v1_alertcategories_create_debug_mode_error_component import (
            ApiV1AlertcategoriesCreateDebugModeErrorComponent,
        )
        from ..models.api_v1_alertcategories_create_description_error_component import (
            ApiV1AlertcategoriesCreateDescriptionErrorComponent,
        )
        from ..models.api_v1_alertcategories_create_display_name_error_component import (
            ApiV1AlertcategoriesCreateDisplayNameErrorComponent,
        )
        from ..models.api_v1_alertcategories_create_kind_error_component import (
            ApiV1AlertcategoriesCreateKindErrorComponent,
        )
        from ..models.api_v1_alertcategories_create_labels_error_component import (
            ApiV1AlertcategoriesCreateLabelsErrorComponent,
        )
        from ..models.api_v1_alertcategories_create_name_error_component import (
            ApiV1AlertcategoriesCreateNameErrorComponent,
        )
        from ..models.api_v1_alertcategories_create_non_field_errors_error_component import (
            ApiV1AlertcategoriesCreateNonFieldErrorsErrorComponent,
        )
        from ..models.api_v1_alertcategories_create_platform_service_error_component import (
            ApiV1AlertcategoriesCreatePlatformServiceErrorComponent,
        )
        from ..models.api_v1_alertcategories_create_provider_error_component import (
            ApiV1AlertcategoriesCreateProviderErrorComponent,
        )
        from ..models.api_v1_alertcategories_create_provider_id_error_component import (
            ApiV1AlertcategoriesCreateProviderIdErrorComponent,
        )
        from ..models.api_v1_alertcategories_create_provider_reference_error_component import (
            ApiV1AlertcategoriesCreateProviderReferenceErrorComponent,
        )
        from ..models.api_v1_alertcategories_create_reconciliation_enabled_error_component import (
            ApiV1AlertcategoriesCreateReconciliationEnabledErrorComponent,
        )
        from ..models.api_v1_alertcategories_create_sla_availability_error_component import (
            ApiV1AlertcategoriesCreateSlaAvailabilityErrorComponent,
        )
        from ..models.api_v1_alertcategories_create_sla_target_error_component import (
            ApiV1AlertcategoriesCreateSlaTargetErrorComponent,
        )
        from ..models.api_v1_alertcategories_create_slo_availability_error_component import (
            ApiV1AlertcategoriesCreateSloAvailabilityErrorComponent,
        )
        from ..models.api_v1_alertcategories_create_slo_target_error_component import (
            ApiV1AlertcategoriesCreateSloTargetErrorComponent,
        )
        from ..models.api_v1_alertcategories_create_sort_order_error_component import (
            ApiV1AlertcategoriesCreateSortOrderErrorComponent,
        )
        from ..models.api_v1_alertcategories_create_target_availability_error_component import (
            ApiV1AlertcategoriesCreateTargetAvailabilityErrorComponent,
        )
        from ..models.api_v1_alertcategories_create_tolerations_error_component import (
            ApiV1AlertcategoriesCreateTolerationsErrorComponent,
        )

        d = dict(src_dict)
        type_ = check_validation_error_enum(d.pop("type"))

        errors = []
        _errors = d.pop("errors")
        for errors_item_data in _errors:

            def _parse_errors_item(
                data: object,
            ) -> (
                ApiV1AlertcategoriesCreateActiveErrorComponent
                | ApiV1AlertcategoriesCreateAnnotationsErrorComponent
                | ApiV1AlertcategoriesCreateArchivedAtErrorComponent
                | ApiV1AlertcategoriesCreateArchivedErrorComponent
                | ApiV1AlertcategoriesCreateArchivedReasonErrorComponent
                | ApiV1AlertcategoriesCreateCriticalityErrorComponent
                | ApiV1AlertcategoriesCreateDebugModeErrorComponent
                | ApiV1AlertcategoriesCreateDescriptionErrorComponent
                | ApiV1AlertcategoriesCreateDisplayNameErrorComponent
                | ApiV1AlertcategoriesCreateKindErrorComponent
                | ApiV1AlertcategoriesCreateLabelsErrorComponent
                | ApiV1AlertcategoriesCreateNameErrorComponent
                | ApiV1AlertcategoriesCreateNonFieldErrorsErrorComponent
                | ApiV1AlertcategoriesCreatePlatformServiceErrorComponent
                | ApiV1AlertcategoriesCreateProviderErrorComponent
                | ApiV1AlertcategoriesCreateProviderIdErrorComponent
                | ApiV1AlertcategoriesCreateProviderReferenceErrorComponent
                | ApiV1AlertcategoriesCreateReconciliationEnabledErrorComponent
                | ApiV1AlertcategoriesCreateSlaAvailabilityErrorComponent
                | ApiV1AlertcategoriesCreateSlaTargetErrorComponent
                | ApiV1AlertcategoriesCreateSloAvailabilityErrorComponent
                | ApiV1AlertcategoriesCreateSloTargetErrorComponent
                | ApiV1AlertcategoriesCreateSortOrderErrorComponent
                | ApiV1AlertcategoriesCreateTargetAvailabilityErrorComponent
                | ApiV1AlertcategoriesCreateTolerationsErrorComponent
            ):
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_alertcategories_create_error_type_0 = (
                        ApiV1AlertcategoriesCreateNonFieldErrorsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_alertcategories_create_error_type_0
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_alertcategories_create_error_type_1 = (
                        ApiV1AlertcategoriesCreateNameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_alertcategories_create_error_type_1
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_alertcategories_create_error_type_2 = (
                        ApiV1AlertcategoriesCreateDisplayNameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_alertcategories_create_error_type_2
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_alertcategories_create_error_type_3 = (
                        ApiV1AlertcategoriesCreateLabelsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_alertcategories_create_error_type_3
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_alertcategories_create_error_type_4 = (
                        ApiV1AlertcategoriesCreateAnnotationsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_alertcategories_create_error_type_4
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_alertcategories_create_error_type_5 = (
                        ApiV1AlertcategoriesCreateDebugModeErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_alertcategories_create_error_type_5
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_alertcategories_create_error_type_6 = (
                        ApiV1AlertcategoriesCreateProviderErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_alertcategories_create_error_type_6
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_alertcategories_create_error_type_7 = (
                        ApiV1AlertcategoriesCreateProviderReferenceErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_alertcategories_create_error_type_7
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_alertcategories_create_error_type_8 = (
                        ApiV1AlertcategoriesCreateProviderIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_alertcategories_create_error_type_8
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_alertcategories_create_error_type_9 = (
                        ApiV1AlertcategoriesCreateReconciliationEnabledErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_alertcategories_create_error_type_9
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_alertcategories_create_error_type_10 = (
                        ApiV1AlertcategoriesCreatePlatformServiceErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_alertcategories_create_error_type_10
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_alertcategories_create_error_type_11 = (
                        ApiV1AlertcategoriesCreateKindErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_alertcategories_create_error_type_11
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_alertcategories_create_error_type_12 = (
                        ApiV1AlertcategoriesCreateTolerationsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_alertcategories_create_error_type_12
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_alertcategories_create_error_type_13 = (
                        ApiV1AlertcategoriesCreateArchivedErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_alertcategories_create_error_type_13
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_alertcategories_create_error_type_14 = (
                        ApiV1AlertcategoriesCreateArchivedAtErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_alertcategories_create_error_type_14
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_alertcategories_create_error_type_15 = (
                        ApiV1AlertcategoriesCreateArchivedReasonErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_alertcategories_create_error_type_15
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_alertcategories_create_error_type_16 = (
                        ApiV1AlertcategoriesCreateCriticalityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_alertcategories_create_error_type_16
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_alertcategories_create_error_type_17 = (
                        ApiV1AlertcategoriesCreateTargetAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_alertcategories_create_error_type_17
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_alertcategories_create_error_type_18 = (
                        ApiV1AlertcategoriesCreateSloTargetErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_alertcategories_create_error_type_18
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_alertcategories_create_error_type_19 = (
                        ApiV1AlertcategoriesCreateSloAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_alertcategories_create_error_type_19
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_alertcategories_create_error_type_20 = (
                        ApiV1AlertcategoriesCreateSlaTargetErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_alertcategories_create_error_type_20
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_alertcategories_create_error_type_21 = (
                        ApiV1AlertcategoriesCreateSlaAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_alertcategories_create_error_type_21
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_alertcategories_create_error_type_22 = (
                        ApiV1AlertcategoriesCreateDescriptionErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_alertcategories_create_error_type_22
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_alertcategories_create_error_type_23 = (
                        ApiV1AlertcategoriesCreateSortOrderErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_alertcategories_create_error_type_23
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_api_v1_alertcategories_create_error_type_24 = (
                    ApiV1AlertcategoriesCreateActiveErrorComponent.from_dict(data)
                )

                return componentsschemas_api_v1_alertcategories_create_error_type_24

            errors_item = _parse_errors_item(errors_item_data)

            errors.append(errors_item)

        api_v1_alertcategories_create_validation_error = cls(
            type_=type_,
            errors=errors,
        )

        api_v1_alertcategories_create_validation_error.additional_properties = d
        return api_v1_alertcategories_create_validation_error

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
