from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.validation_error_enum import ValidationErrorEnum, check_validation_error_enum

if TYPE_CHECKING:
    from ..models.api_v1_alertcategories_archive_create_active_error_component import (
        ApiV1AlertcategoriesArchiveCreateActiveErrorComponent,
    )
    from ..models.api_v1_alertcategories_archive_create_annotations_error_component import (
        ApiV1AlertcategoriesArchiveCreateAnnotationsErrorComponent,
    )
    from ..models.api_v1_alertcategories_archive_create_archived_at_error_component import (
        ApiV1AlertcategoriesArchiveCreateArchivedAtErrorComponent,
    )
    from ..models.api_v1_alertcategories_archive_create_archived_error_component import (
        ApiV1AlertcategoriesArchiveCreateArchivedErrorComponent,
    )
    from ..models.api_v1_alertcategories_archive_create_archived_reason_error_component import (
        ApiV1AlertcategoriesArchiveCreateArchivedReasonErrorComponent,
    )
    from ..models.api_v1_alertcategories_archive_create_criticality_error_component import (
        ApiV1AlertcategoriesArchiveCreateCriticalityErrorComponent,
    )
    from ..models.api_v1_alertcategories_archive_create_debug_mode_error_component import (
        ApiV1AlertcategoriesArchiveCreateDebugModeErrorComponent,
    )
    from ..models.api_v1_alertcategories_archive_create_description_error_component import (
        ApiV1AlertcategoriesArchiveCreateDescriptionErrorComponent,
    )
    from ..models.api_v1_alertcategories_archive_create_display_name_error_component import (
        ApiV1AlertcategoriesArchiveCreateDisplayNameErrorComponent,
    )
    from ..models.api_v1_alertcategories_archive_create_kind_error_component import (
        ApiV1AlertcategoriesArchiveCreateKindErrorComponent,
    )
    from ..models.api_v1_alertcategories_archive_create_labels_error_component import (
        ApiV1AlertcategoriesArchiveCreateLabelsErrorComponent,
    )
    from ..models.api_v1_alertcategories_archive_create_name_error_component import (
        ApiV1AlertcategoriesArchiveCreateNameErrorComponent,
    )
    from ..models.api_v1_alertcategories_archive_create_non_field_errors_error_component import (
        ApiV1AlertcategoriesArchiveCreateNonFieldErrorsErrorComponent,
    )
    from ..models.api_v1_alertcategories_archive_create_platform_service_error_component import (
        ApiV1AlertcategoriesArchiveCreatePlatformServiceErrorComponent,
    )
    from ..models.api_v1_alertcategories_archive_create_provider_error_component import (
        ApiV1AlertcategoriesArchiveCreateProviderErrorComponent,
    )
    from ..models.api_v1_alertcategories_archive_create_provider_id_error_component import (
        ApiV1AlertcategoriesArchiveCreateProviderIdErrorComponent,
    )
    from ..models.api_v1_alertcategories_archive_create_provider_reference_error_component import (
        ApiV1AlertcategoriesArchiveCreateProviderReferenceErrorComponent,
    )
    from ..models.api_v1_alertcategories_archive_create_reconciliation_enabled_error_component import (
        ApiV1AlertcategoriesArchiveCreateReconciliationEnabledErrorComponent,
    )
    from ..models.api_v1_alertcategories_archive_create_sla_availability_error_component import (
        ApiV1AlertcategoriesArchiveCreateSlaAvailabilityErrorComponent,
    )
    from ..models.api_v1_alertcategories_archive_create_sla_target_error_component import (
        ApiV1AlertcategoriesArchiveCreateSlaTargetErrorComponent,
    )
    from ..models.api_v1_alertcategories_archive_create_slo_availability_error_component import (
        ApiV1AlertcategoriesArchiveCreateSloAvailabilityErrorComponent,
    )
    from ..models.api_v1_alertcategories_archive_create_slo_target_error_component import (
        ApiV1AlertcategoriesArchiveCreateSloTargetErrorComponent,
    )
    from ..models.api_v1_alertcategories_archive_create_sort_order_error_component import (
        ApiV1AlertcategoriesArchiveCreateSortOrderErrorComponent,
    )
    from ..models.api_v1_alertcategories_archive_create_target_availability_error_component import (
        ApiV1AlertcategoriesArchiveCreateTargetAvailabilityErrorComponent,
    )
    from ..models.api_v1_alertcategories_archive_create_tolerations_error_component import (
        ApiV1AlertcategoriesArchiveCreateTolerationsErrorComponent,
    )


T = TypeVar("T", bound="ApiV1AlertcategoriesArchiveCreateValidationError")


@_attrs_define
class ApiV1AlertcategoriesArchiveCreateValidationError:
    """
    Attributes:
        type_ (ValidationErrorEnum): * `validation_error` - Validation Error
        errors (list[ApiV1AlertcategoriesArchiveCreateActiveErrorComponent |
            ApiV1AlertcategoriesArchiveCreateAnnotationsErrorComponent |
            ApiV1AlertcategoriesArchiveCreateArchivedAtErrorComponent |
            ApiV1AlertcategoriesArchiveCreateArchivedErrorComponent |
            ApiV1AlertcategoriesArchiveCreateArchivedReasonErrorComponent |
            ApiV1AlertcategoriesArchiveCreateCriticalityErrorComponent |
            ApiV1AlertcategoriesArchiveCreateDebugModeErrorComponent |
            ApiV1AlertcategoriesArchiveCreateDescriptionErrorComponent |
            ApiV1AlertcategoriesArchiveCreateDisplayNameErrorComponent | ApiV1AlertcategoriesArchiveCreateKindErrorComponent
            | ApiV1AlertcategoriesArchiveCreateLabelsErrorComponent | ApiV1AlertcategoriesArchiveCreateNameErrorComponent |
            ApiV1AlertcategoriesArchiveCreateNonFieldErrorsErrorComponent |
            ApiV1AlertcategoriesArchiveCreatePlatformServiceErrorComponent |
            ApiV1AlertcategoriesArchiveCreateProviderErrorComponent |
            ApiV1AlertcategoriesArchiveCreateProviderIdErrorComponent |
            ApiV1AlertcategoriesArchiveCreateProviderReferenceErrorComponent |
            ApiV1AlertcategoriesArchiveCreateReconciliationEnabledErrorComponent |
            ApiV1AlertcategoriesArchiveCreateSlaAvailabilityErrorComponent |
            ApiV1AlertcategoriesArchiveCreateSlaTargetErrorComponent |
            ApiV1AlertcategoriesArchiveCreateSloAvailabilityErrorComponent |
            ApiV1AlertcategoriesArchiveCreateSloTargetErrorComponent |
            ApiV1AlertcategoriesArchiveCreateSortOrderErrorComponent |
            ApiV1AlertcategoriesArchiveCreateTargetAvailabilityErrorComponent |
            ApiV1AlertcategoriesArchiveCreateTolerationsErrorComponent]):
    """

    type_: ValidationErrorEnum
    errors: list[
        ApiV1AlertcategoriesArchiveCreateActiveErrorComponent
        | ApiV1AlertcategoriesArchiveCreateAnnotationsErrorComponent
        | ApiV1AlertcategoriesArchiveCreateArchivedAtErrorComponent
        | ApiV1AlertcategoriesArchiveCreateArchivedErrorComponent
        | ApiV1AlertcategoriesArchiveCreateArchivedReasonErrorComponent
        | ApiV1AlertcategoriesArchiveCreateCriticalityErrorComponent
        | ApiV1AlertcategoriesArchiveCreateDebugModeErrorComponent
        | ApiV1AlertcategoriesArchiveCreateDescriptionErrorComponent
        | ApiV1AlertcategoriesArchiveCreateDisplayNameErrorComponent
        | ApiV1AlertcategoriesArchiveCreateKindErrorComponent
        | ApiV1AlertcategoriesArchiveCreateLabelsErrorComponent
        | ApiV1AlertcategoriesArchiveCreateNameErrorComponent
        | ApiV1AlertcategoriesArchiveCreateNonFieldErrorsErrorComponent
        | ApiV1AlertcategoriesArchiveCreatePlatformServiceErrorComponent
        | ApiV1AlertcategoriesArchiveCreateProviderErrorComponent
        | ApiV1AlertcategoriesArchiveCreateProviderIdErrorComponent
        | ApiV1AlertcategoriesArchiveCreateProviderReferenceErrorComponent
        | ApiV1AlertcategoriesArchiveCreateReconciliationEnabledErrorComponent
        | ApiV1AlertcategoriesArchiveCreateSlaAvailabilityErrorComponent
        | ApiV1AlertcategoriesArchiveCreateSlaTargetErrorComponent
        | ApiV1AlertcategoriesArchiveCreateSloAvailabilityErrorComponent
        | ApiV1AlertcategoriesArchiveCreateSloTargetErrorComponent
        | ApiV1AlertcategoriesArchiveCreateSortOrderErrorComponent
        | ApiV1AlertcategoriesArchiveCreateTargetAvailabilityErrorComponent
        | ApiV1AlertcategoriesArchiveCreateTolerationsErrorComponent
    ]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.api_v1_alertcategories_archive_create_annotations_error_component import (
            ApiV1AlertcategoriesArchiveCreateAnnotationsErrorComponent,
        )
        from ..models.api_v1_alertcategories_archive_create_archived_at_error_component import (
            ApiV1AlertcategoriesArchiveCreateArchivedAtErrorComponent,
        )
        from ..models.api_v1_alertcategories_archive_create_archived_error_component import (
            ApiV1AlertcategoriesArchiveCreateArchivedErrorComponent,
        )
        from ..models.api_v1_alertcategories_archive_create_archived_reason_error_component import (
            ApiV1AlertcategoriesArchiveCreateArchivedReasonErrorComponent,
        )
        from ..models.api_v1_alertcategories_archive_create_criticality_error_component import (
            ApiV1AlertcategoriesArchiveCreateCriticalityErrorComponent,
        )
        from ..models.api_v1_alertcategories_archive_create_debug_mode_error_component import (
            ApiV1AlertcategoriesArchiveCreateDebugModeErrorComponent,
        )
        from ..models.api_v1_alertcategories_archive_create_description_error_component import (
            ApiV1AlertcategoriesArchiveCreateDescriptionErrorComponent,
        )
        from ..models.api_v1_alertcategories_archive_create_display_name_error_component import (
            ApiV1AlertcategoriesArchiveCreateDisplayNameErrorComponent,
        )
        from ..models.api_v1_alertcategories_archive_create_kind_error_component import (
            ApiV1AlertcategoriesArchiveCreateKindErrorComponent,
        )
        from ..models.api_v1_alertcategories_archive_create_labels_error_component import (
            ApiV1AlertcategoriesArchiveCreateLabelsErrorComponent,
        )
        from ..models.api_v1_alertcategories_archive_create_name_error_component import (
            ApiV1AlertcategoriesArchiveCreateNameErrorComponent,
        )
        from ..models.api_v1_alertcategories_archive_create_non_field_errors_error_component import (
            ApiV1AlertcategoriesArchiveCreateNonFieldErrorsErrorComponent,
        )
        from ..models.api_v1_alertcategories_archive_create_platform_service_error_component import (
            ApiV1AlertcategoriesArchiveCreatePlatformServiceErrorComponent,
        )
        from ..models.api_v1_alertcategories_archive_create_provider_error_component import (
            ApiV1AlertcategoriesArchiveCreateProviderErrorComponent,
        )
        from ..models.api_v1_alertcategories_archive_create_provider_id_error_component import (
            ApiV1AlertcategoriesArchiveCreateProviderIdErrorComponent,
        )
        from ..models.api_v1_alertcategories_archive_create_provider_reference_error_component import (
            ApiV1AlertcategoriesArchiveCreateProviderReferenceErrorComponent,
        )
        from ..models.api_v1_alertcategories_archive_create_reconciliation_enabled_error_component import (
            ApiV1AlertcategoriesArchiveCreateReconciliationEnabledErrorComponent,
        )
        from ..models.api_v1_alertcategories_archive_create_sla_availability_error_component import (
            ApiV1AlertcategoriesArchiveCreateSlaAvailabilityErrorComponent,
        )
        from ..models.api_v1_alertcategories_archive_create_sla_target_error_component import (
            ApiV1AlertcategoriesArchiveCreateSlaTargetErrorComponent,
        )
        from ..models.api_v1_alertcategories_archive_create_slo_availability_error_component import (
            ApiV1AlertcategoriesArchiveCreateSloAvailabilityErrorComponent,
        )
        from ..models.api_v1_alertcategories_archive_create_slo_target_error_component import (
            ApiV1AlertcategoriesArchiveCreateSloTargetErrorComponent,
        )
        from ..models.api_v1_alertcategories_archive_create_sort_order_error_component import (
            ApiV1AlertcategoriesArchiveCreateSortOrderErrorComponent,
        )
        from ..models.api_v1_alertcategories_archive_create_target_availability_error_component import (
            ApiV1AlertcategoriesArchiveCreateTargetAvailabilityErrorComponent,
        )
        from ..models.api_v1_alertcategories_archive_create_tolerations_error_component import (
            ApiV1AlertcategoriesArchiveCreateTolerationsErrorComponent,
        )

        type_: str = self.type_

        errors = []
        for errors_item_data in self.errors:
            errors_item: dict[str, Any]
            if isinstance(errors_item_data, ApiV1AlertcategoriesArchiveCreateNonFieldErrorsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1AlertcategoriesArchiveCreateNameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1AlertcategoriesArchiveCreateDisplayNameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1AlertcategoriesArchiveCreateLabelsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1AlertcategoriesArchiveCreateAnnotationsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1AlertcategoriesArchiveCreateDebugModeErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1AlertcategoriesArchiveCreateProviderErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1AlertcategoriesArchiveCreateProviderReferenceErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1AlertcategoriesArchiveCreateProviderIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1AlertcategoriesArchiveCreateReconciliationEnabledErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1AlertcategoriesArchiveCreatePlatformServiceErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1AlertcategoriesArchiveCreateKindErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1AlertcategoriesArchiveCreateTolerationsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1AlertcategoriesArchiveCreateArchivedErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1AlertcategoriesArchiveCreateArchivedAtErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1AlertcategoriesArchiveCreateArchivedReasonErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1AlertcategoriesArchiveCreateCriticalityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1AlertcategoriesArchiveCreateTargetAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1AlertcategoriesArchiveCreateSloTargetErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1AlertcategoriesArchiveCreateSloAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1AlertcategoriesArchiveCreateSlaTargetErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1AlertcategoriesArchiveCreateSlaAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1AlertcategoriesArchiveCreateDescriptionErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1AlertcategoriesArchiveCreateSortOrderErrorComponent):
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
        from ..models.api_v1_alertcategories_archive_create_active_error_component import (
            ApiV1AlertcategoriesArchiveCreateActiveErrorComponent,
        )
        from ..models.api_v1_alertcategories_archive_create_annotations_error_component import (
            ApiV1AlertcategoriesArchiveCreateAnnotationsErrorComponent,
        )
        from ..models.api_v1_alertcategories_archive_create_archived_at_error_component import (
            ApiV1AlertcategoriesArchiveCreateArchivedAtErrorComponent,
        )
        from ..models.api_v1_alertcategories_archive_create_archived_error_component import (
            ApiV1AlertcategoriesArchiveCreateArchivedErrorComponent,
        )
        from ..models.api_v1_alertcategories_archive_create_archived_reason_error_component import (
            ApiV1AlertcategoriesArchiveCreateArchivedReasonErrorComponent,
        )
        from ..models.api_v1_alertcategories_archive_create_criticality_error_component import (
            ApiV1AlertcategoriesArchiveCreateCriticalityErrorComponent,
        )
        from ..models.api_v1_alertcategories_archive_create_debug_mode_error_component import (
            ApiV1AlertcategoriesArchiveCreateDebugModeErrorComponent,
        )
        from ..models.api_v1_alertcategories_archive_create_description_error_component import (
            ApiV1AlertcategoriesArchiveCreateDescriptionErrorComponent,
        )
        from ..models.api_v1_alertcategories_archive_create_display_name_error_component import (
            ApiV1AlertcategoriesArchiveCreateDisplayNameErrorComponent,
        )
        from ..models.api_v1_alertcategories_archive_create_kind_error_component import (
            ApiV1AlertcategoriesArchiveCreateKindErrorComponent,
        )
        from ..models.api_v1_alertcategories_archive_create_labels_error_component import (
            ApiV1AlertcategoriesArchiveCreateLabelsErrorComponent,
        )
        from ..models.api_v1_alertcategories_archive_create_name_error_component import (
            ApiV1AlertcategoriesArchiveCreateNameErrorComponent,
        )
        from ..models.api_v1_alertcategories_archive_create_non_field_errors_error_component import (
            ApiV1AlertcategoriesArchiveCreateNonFieldErrorsErrorComponent,
        )
        from ..models.api_v1_alertcategories_archive_create_platform_service_error_component import (
            ApiV1AlertcategoriesArchiveCreatePlatformServiceErrorComponent,
        )
        from ..models.api_v1_alertcategories_archive_create_provider_error_component import (
            ApiV1AlertcategoriesArchiveCreateProviderErrorComponent,
        )
        from ..models.api_v1_alertcategories_archive_create_provider_id_error_component import (
            ApiV1AlertcategoriesArchiveCreateProviderIdErrorComponent,
        )
        from ..models.api_v1_alertcategories_archive_create_provider_reference_error_component import (
            ApiV1AlertcategoriesArchiveCreateProviderReferenceErrorComponent,
        )
        from ..models.api_v1_alertcategories_archive_create_reconciliation_enabled_error_component import (
            ApiV1AlertcategoriesArchiveCreateReconciliationEnabledErrorComponent,
        )
        from ..models.api_v1_alertcategories_archive_create_sla_availability_error_component import (
            ApiV1AlertcategoriesArchiveCreateSlaAvailabilityErrorComponent,
        )
        from ..models.api_v1_alertcategories_archive_create_sla_target_error_component import (
            ApiV1AlertcategoriesArchiveCreateSlaTargetErrorComponent,
        )
        from ..models.api_v1_alertcategories_archive_create_slo_availability_error_component import (
            ApiV1AlertcategoriesArchiveCreateSloAvailabilityErrorComponent,
        )
        from ..models.api_v1_alertcategories_archive_create_slo_target_error_component import (
            ApiV1AlertcategoriesArchiveCreateSloTargetErrorComponent,
        )
        from ..models.api_v1_alertcategories_archive_create_sort_order_error_component import (
            ApiV1AlertcategoriesArchiveCreateSortOrderErrorComponent,
        )
        from ..models.api_v1_alertcategories_archive_create_target_availability_error_component import (
            ApiV1AlertcategoriesArchiveCreateTargetAvailabilityErrorComponent,
        )
        from ..models.api_v1_alertcategories_archive_create_tolerations_error_component import (
            ApiV1AlertcategoriesArchiveCreateTolerationsErrorComponent,
        )

        d = dict(src_dict)
        type_ = check_validation_error_enum(d.pop("type"))

        errors = []
        _errors = d.pop("errors")
        for errors_item_data in _errors:

            def _parse_errors_item(
                data: object,
            ) -> (
                ApiV1AlertcategoriesArchiveCreateActiveErrorComponent
                | ApiV1AlertcategoriesArchiveCreateAnnotationsErrorComponent
                | ApiV1AlertcategoriesArchiveCreateArchivedAtErrorComponent
                | ApiV1AlertcategoriesArchiveCreateArchivedErrorComponent
                | ApiV1AlertcategoriesArchiveCreateArchivedReasonErrorComponent
                | ApiV1AlertcategoriesArchiveCreateCriticalityErrorComponent
                | ApiV1AlertcategoriesArchiveCreateDebugModeErrorComponent
                | ApiV1AlertcategoriesArchiveCreateDescriptionErrorComponent
                | ApiV1AlertcategoriesArchiveCreateDisplayNameErrorComponent
                | ApiV1AlertcategoriesArchiveCreateKindErrorComponent
                | ApiV1AlertcategoriesArchiveCreateLabelsErrorComponent
                | ApiV1AlertcategoriesArchiveCreateNameErrorComponent
                | ApiV1AlertcategoriesArchiveCreateNonFieldErrorsErrorComponent
                | ApiV1AlertcategoriesArchiveCreatePlatformServiceErrorComponent
                | ApiV1AlertcategoriesArchiveCreateProviderErrorComponent
                | ApiV1AlertcategoriesArchiveCreateProviderIdErrorComponent
                | ApiV1AlertcategoriesArchiveCreateProviderReferenceErrorComponent
                | ApiV1AlertcategoriesArchiveCreateReconciliationEnabledErrorComponent
                | ApiV1AlertcategoriesArchiveCreateSlaAvailabilityErrorComponent
                | ApiV1AlertcategoriesArchiveCreateSlaTargetErrorComponent
                | ApiV1AlertcategoriesArchiveCreateSloAvailabilityErrorComponent
                | ApiV1AlertcategoriesArchiveCreateSloTargetErrorComponent
                | ApiV1AlertcategoriesArchiveCreateSortOrderErrorComponent
                | ApiV1AlertcategoriesArchiveCreateTargetAvailabilityErrorComponent
                | ApiV1AlertcategoriesArchiveCreateTolerationsErrorComponent
            ):
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_alertcategories_archive_create_error_type_0 = (
                        ApiV1AlertcategoriesArchiveCreateNonFieldErrorsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_alertcategories_archive_create_error_type_0
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_alertcategories_archive_create_error_type_1 = (
                        ApiV1AlertcategoriesArchiveCreateNameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_alertcategories_archive_create_error_type_1
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_alertcategories_archive_create_error_type_2 = (
                        ApiV1AlertcategoriesArchiveCreateDisplayNameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_alertcategories_archive_create_error_type_2
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_alertcategories_archive_create_error_type_3 = (
                        ApiV1AlertcategoriesArchiveCreateLabelsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_alertcategories_archive_create_error_type_3
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_alertcategories_archive_create_error_type_4 = (
                        ApiV1AlertcategoriesArchiveCreateAnnotationsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_alertcategories_archive_create_error_type_4
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_alertcategories_archive_create_error_type_5 = (
                        ApiV1AlertcategoriesArchiveCreateDebugModeErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_alertcategories_archive_create_error_type_5
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_alertcategories_archive_create_error_type_6 = (
                        ApiV1AlertcategoriesArchiveCreateProviderErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_alertcategories_archive_create_error_type_6
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_alertcategories_archive_create_error_type_7 = (
                        ApiV1AlertcategoriesArchiveCreateProviderReferenceErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_alertcategories_archive_create_error_type_7
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_alertcategories_archive_create_error_type_8 = (
                        ApiV1AlertcategoriesArchiveCreateProviderIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_alertcategories_archive_create_error_type_8
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_alertcategories_archive_create_error_type_9 = (
                        ApiV1AlertcategoriesArchiveCreateReconciliationEnabledErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_alertcategories_archive_create_error_type_9
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_alertcategories_archive_create_error_type_10 = (
                        ApiV1AlertcategoriesArchiveCreatePlatformServiceErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_alertcategories_archive_create_error_type_10
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_alertcategories_archive_create_error_type_11 = (
                        ApiV1AlertcategoriesArchiveCreateKindErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_alertcategories_archive_create_error_type_11
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_alertcategories_archive_create_error_type_12 = (
                        ApiV1AlertcategoriesArchiveCreateTolerationsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_alertcategories_archive_create_error_type_12
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_alertcategories_archive_create_error_type_13 = (
                        ApiV1AlertcategoriesArchiveCreateArchivedErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_alertcategories_archive_create_error_type_13
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_alertcategories_archive_create_error_type_14 = (
                        ApiV1AlertcategoriesArchiveCreateArchivedAtErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_alertcategories_archive_create_error_type_14
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_alertcategories_archive_create_error_type_15 = (
                        ApiV1AlertcategoriesArchiveCreateArchivedReasonErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_alertcategories_archive_create_error_type_15
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_alertcategories_archive_create_error_type_16 = (
                        ApiV1AlertcategoriesArchiveCreateCriticalityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_alertcategories_archive_create_error_type_16
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_alertcategories_archive_create_error_type_17 = (
                        ApiV1AlertcategoriesArchiveCreateTargetAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_alertcategories_archive_create_error_type_17
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_alertcategories_archive_create_error_type_18 = (
                        ApiV1AlertcategoriesArchiveCreateSloTargetErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_alertcategories_archive_create_error_type_18
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_alertcategories_archive_create_error_type_19 = (
                        ApiV1AlertcategoriesArchiveCreateSloAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_alertcategories_archive_create_error_type_19
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_alertcategories_archive_create_error_type_20 = (
                        ApiV1AlertcategoriesArchiveCreateSlaTargetErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_alertcategories_archive_create_error_type_20
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_alertcategories_archive_create_error_type_21 = (
                        ApiV1AlertcategoriesArchiveCreateSlaAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_alertcategories_archive_create_error_type_21
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_alertcategories_archive_create_error_type_22 = (
                        ApiV1AlertcategoriesArchiveCreateDescriptionErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_alertcategories_archive_create_error_type_22
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_alertcategories_archive_create_error_type_23 = (
                        ApiV1AlertcategoriesArchiveCreateSortOrderErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_alertcategories_archive_create_error_type_23
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_api_v1_alertcategories_archive_create_error_type_24 = (
                    ApiV1AlertcategoriesArchiveCreateActiveErrorComponent.from_dict(data)
                )

                return componentsschemas_api_v1_alertcategories_archive_create_error_type_24

            errors_item = _parse_errors_item(errors_item_data)

            errors.append(errors_item)

        api_v1_alertcategories_archive_create_validation_error = cls(
            type_=type_,
            errors=errors,
        )

        api_v1_alertcategories_archive_create_validation_error.additional_properties = d
        return api_v1_alertcategories_archive_create_validation_error

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
