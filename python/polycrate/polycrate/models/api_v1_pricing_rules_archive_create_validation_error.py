from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.validation_error_enum import ValidationErrorEnum, check_validation_error_enum

if TYPE_CHECKING:
    from ..models.api_v1_pricing_rules_archive_create_active_from_error_component import (
        ApiV1PricingRulesArchiveCreateActiveFromErrorComponent,
    )
    from ..models.api_v1_pricing_rules_archive_create_active_until_error_component import (
        ApiV1PricingRulesArchiveCreateActiveUntilErrorComponent,
    )
    from ..models.api_v1_pricing_rules_archive_create_annotations_error_component import (
        ApiV1PricingRulesArchiveCreateAnnotationsErrorComponent,
    )
    from ..models.api_v1_pricing_rules_archive_create_archived_at_error_component import (
        ApiV1PricingRulesArchiveCreateArchivedAtErrorComponent,
    )
    from ..models.api_v1_pricing_rules_archive_create_archived_error_component import (
        ApiV1PricingRulesArchiveCreateArchivedErrorComponent,
    )
    from ..models.api_v1_pricing_rules_archive_create_archived_reason_error_component import (
        ApiV1PricingRulesArchiveCreateArchivedReasonErrorComponent,
    )
    from ..models.api_v1_pricing_rules_archive_create_criticality_error_component import (
        ApiV1PricingRulesArchiveCreateCriticalityErrorComponent,
    )
    from ..models.api_v1_pricing_rules_archive_create_debug_mode_error_component import (
        ApiV1PricingRulesArchiveCreateDebugModeErrorComponent,
    )
    from ..models.api_v1_pricing_rules_archive_create_discount_type_error_component import (
        ApiV1PricingRulesArchiveCreateDiscountTypeErrorComponent,
    )
    from ..models.api_v1_pricing_rules_archive_create_discount_value_error_component import (
        ApiV1PricingRulesArchiveCreateDiscountValueErrorComponent,
    )
    from ..models.api_v1_pricing_rules_archive_create_display_name_error_component import (
        ApiV1PricingRulesArchiveCreateDisplayNameErrorComponent,
    )
    from ..models.api_v1_pricing_rules_archive_create_kind_error_component import (
        ApiV1PricingRulesArchiveCreateKindErrorComponent,
    )
    from ..models.api_v1_pricing_rules_archive_create_labels_error_component import (
        ApiV1PricingRulesArchiveCreateLabelsErrorComponent,
    )
    from ..models.api_v1_pricing_rules_archive_create_name_error_component import (
        ApiV1PricingRulesArchiveCreateNameErrorComponent,
    )
    from ..models.api_v1_pricing_rules_archive_create_non_field_errors_error_component import (
        ApiV1PricingRulesArchiveCreateNonFieldErrorsErrorComponent,
    )
    from ..models.api_v1_pricing_rules_archive_create_platform_service_error_component import (
        ApiV1PricingRulesArchiveCreatePlatformServiceErrorComponent,
    )
    from ..models.api_v1_pricing_rules_archive_create_product_kind_error_component import (
        ApiV1PricingRulesArchiveCreateProductKindErrorComponent,
    )
    from ..models.api_v1_pricing_rules_archive_create_provider_error_component import (
        ApiV1PricingRulesArchiveCreateProviderErrorComponent,
    )
    from ..models.api_v1_pricing_rules_archive_create_provider_id_error_component import (
        ApiV1PricingRulesArchiveCreateProviderIdErrorComponent,
    )
    from ..models.api_v1_pricing_rules_archive_create_provider_reference_error_component import (
        ApiV1PricingRulesArchiveCreateProviderReferenceErrorComponent,
    )
    from ..models.api_v1_pricing_rules_archive_create_reconciliation_enabled_error_component import (
        ApiV1PricingRulesArchiveCreateReconciliationEnabledErrorComponent,
    )
    from ..models.api_v1_pricing_rules_archive_create_sla_availability_error_component import (
        ApiV1PricingRulesArchiveCreateSlaAvailabilityErrorComponent,
    )
    from ..models.api_v1_pricing_rules_archive_create_sla_target_error_component import (
        ApiV1PricingRulesArchiveCreateSlaTargetErrorComponent,
    )
    from ..models.api_v1_pricing_rules_archive_create_slo_availability_error_component import (
        ApiV1PricingRulesArchiveCreateSloAvailabilityErrorComponent,
    )
    from ..models.api_v1_pricing_rules_archive_create_slo_target_error_component import (
        ApiV1PricingRulesArchiveCreateSloTargetErrorComponent,
    )
    from ..models.api_v1_pricing_rules_archive_create_target_availability_error_component import (
        ApiV1PricingRulesArchiveCreateTargetAvailabilityErrorComponent,
    )
    from ..models.api_v1_pricing_rules_archive_create_tolerations_error_component import (
        ApiV1PricingRulesArchiveCreateTolerationsErrorComponent,
    )


T = TypeVar("T", bound="ApiV1PricingRulesArchiveCreateValidationError")


@_attrs_define
class ApiV1PricingRulesArchiveCreateValidationError:
    """
    Attributes:
        type_ (ValidationErrorEnum): * `validation_error` - Validation Error
        errors (list[ApiV1PricingRulesArchiveCreateActiveFromErrorComponent |
            ApiV1PricingRulesArchiveCreateActiveUntilErrorComponent |
            ApiV1PricingRulesArchiveCreateAnnotationsErrorComponent | ApiV1PricingRulesArchiveCreateArchivedAtErrorComponent
            | ApiV1PricingRulesArchiveCreateArchivedErrorComponent |
            ApiV1PricingRulesArchiveCreateArchivedReasonErrorComponent |
            ApiV1PricingRulesArchiveCreateCriticalityErrorComponent | ApiV1PricingRulesArchiveCreateDebugModeErrorComponent
            | ApiV1PricingRulesArchiveCreateDiscountTypeErrorComponent |
            ApiV1PricingRulesArchiveCreateDiscountValueErrorComponent |
            ApiV1PricingRulesArchiveCreateDisplayNameErrorComponent | ApiV1PricingRulesArchiveCreateKindErrorComponent |
            ApiV1PricingRulesArchiveCreateLabelsErrorComponent | ApiV1PricingRulesArchiveCreateNameErrorComponent |
            ApiV1PricingRulesArchiveCreateNonFieldErrorsErrorComponent |
            ApiV1PricingRulesArchiveCreatePlatformServiceErrorComponent |
            ApiV1PricingRulesArchiveCreateProductKindErrorComponent | ApiV1PricingRulesArchiveCreateProviderErrorComponent |
            ApiV1PricingRulesArchiveCreateProviderIdErrorComponent |
            ApiV1PricingRulesArchiveCreateProviderReferenceErrorComponent |
            ApiV1PricingRulesArchiveCreateReconciliationEnabledErrorComponent |
            ApiV1PricingRulesArchiveCreateSlaAvailabilityErrorComponent |
            ApiV1PricingRulesArchiveCreateSlaTargetErrorComponent |
            ApiV1PricingRulesArchiveCreateSloAvailabilityErrorComponent |
            ApiV1PricingRulesArchiveCreateSloTargetErrorComponent |
            ApiV1PricingRulesArchiveCreateTargetAvailabilityErrorComponent |
            ApiV1PricingRulesArchiveCreateTolerationsErrorComponent]):
    """

    type_: ValidationErrorEnum
    errors: list[
        ApiV1PricingRulesArchiveCreateActiveFromErrorComponent
        | ApiV1PricingRulesArchiveCreateActiveUntilErrorComponent
        | ApiV1PricingRulesArchiveCreateAnnotationsErrorComponent
        | ApiV1PricingRulesArchiveCreateArchivedAtErrorComponent
        | ApiV1PricingRulesArchiveCreateArchivedErrorComponent
        | ApiV1PricingRulesArchiveCreateArchivedReasonErrorComponent
        | ApiV1PricingRulesArchiveCreateCriticalityErrorComponent
        | ApiV1PricingRulesArchiveCreateDebugModeErrorComponent
        | ApiV1PricingRulesArchiveCreateDiscountTypeErrorComponent
        | ApiV1PricingRulesArchiveCreateDiscountValueErrorComponent
        | ApiV1PricingRulesArchiveCreateDisplayNameErrorComponent
        | ApiV1PricingRulesArchiveCreateKindErrorComponent
        | ApiV1PricingRulesArchiveCreateLabelsErrorComponent
        | ApiV1PricingRulesArchiveCreateNameErrorComponent
        | ApiV1PricingRulesArchiveCreateNonFieldErrorsErrorComponent
        | ApiV1PricingRulesArchiveCreatePlatformServiceErrorComponent
        | ApiV1PricingRulesArchiveCreateProductKindErrorComponent
        | ApiV1PricingRulesArchiveCreateProviderErrorComponent
        | ApiV1PricingRulesArchiveCreateProviderIdErrorComponent
        | ApiV1PricingRulesArchiveCreateProviderReferenceErrorComponent
        | ApiV1PricingRulesArchiveCreateReconciliationEnabledErrorComponent
        | ApiV1PricingRulesArchiveCreateSlaAvailabilityErrorComponent
        | ApiV1PricingRulesArchiveCreateSlaTargetErrorComponent
        | ApiV1PricingRulesArchiveCreateSloAvailabilityErrorComponent
        | ApiV1PricingRulesArchiveCreateSloTargetErrorComponent
        | ApiV1PricingRulesArchiveCreateTargetAvailabilityErrorComponent
        | ApiV1PricingRulesArchiveCreateTolerationsErrorComponent
    ]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.api_v1_pricing_rules_archive_create_active_from_error_component import (
            ApiV1PricingRulesArchiveCreateActiveFromErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_rules_archive_create_annotations_error_component import (
            ApiV1PricingRulesArchiveCreateAnnotationsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_rules_archive_create_archived_at_error_component import (
            ApiV1PricingRulesArchiveCreateArchivedAtErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_rules_archive_create_archived_error_component import (
            ApiV1PricingRulesArchiveCreateArchivedErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_rules_archive_create_archived_reason_error_component import (
            ApiV1PricingRulesArchiveCreateArchivedReasonErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_rules_archive_create_criticality_error_component import (
            ApiV1PricingRulesArchiveCreateCriticalityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_rules_archive_create_debug_mode_error_component import (
            ApiV1PricingRulesArchiveCreateDebugModeErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_rules_archive_create_discount_type_error_component import (
            ApiV1PricingRulesArchiveCreateDiscountTypeErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_rules_archive_create_discount_value_error_component import (
            ApiV1PricingRulesArchiveCreateDiscountValueErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_rules_archive_create_display_name_error_component import (
            ApiV1PricingRulesArchiveCreateDisplayNameErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_rules_archive_create_kind_error_component import (
            ApiV1PricingRulesArchiveCreateKindErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_rules_archive_create_labels_error_component import (
            ApiV1PricingRulesArchiveCreateLabelsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_rules_archive_create_name_error_component import (
            ApiV1PricingRulesArchiveCreateNameErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_rules_archive_create_non_field_errors_error_component import (
            ApiV1PricingRulesArchiveCreateNonFieldErrorsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_rules_archive_create_platform_service_error_component import (
            ApiV1PricingRulesArchiveCreatePlatformServiceErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_rules_archive_create_product_kind_error_component import (
            ApiV1PricingRulesArchiveCreateProductKindErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_rules_archive_create_provider_error_component import (
            ApiV1PricingRulesArchiveCreateProviderErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_rules_archive_create_provider_id_error_component import (
            ApiV1PricingRulesArchiveCreateProviderIdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_rules_archive_create_provider_reference_error_component import (
            ApiV1PricingRulesArchiveCreateProviderReferenceErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_rules_archive_create_reconciliation_enabled_error_component import (
            ApiV1PricingRulesArchiveCreateReconciliationEnabledErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_rules_archive_create_sla_availability_error_component import (
            ApiV1PricingRulesArchiveCreateSlaAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_rules_archive_create_sla_target_error_component import (
            ApiV1PricingRulesArchiveCreateSlaTargetErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_rules_archive_create_slo_availability_error_component import (
            ApiV1PricingRulesArchiveCreateSloAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_rules_archive_create_slo_target_error_component import (
            ApiV1PricingRulesArchiveCreateSloTargetErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_rules_archive_create_target_availability_error_component import (
            ApiV1PricingRulesArchiveCreateTargetAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_rules_archive_create_tolerations_error_component import (
            ApiV1PricingRulesArchiveCreateTolerationsErrorComponent,  # noqa: PLC0415
        )

        type_: str = self.type_

        errors = []
        for errors_item_data in self.errors:
            errors_item: dict[str, Any]
            if isinstance(errors_item_data, ApiV1PricingRulesArchiveCreateNonFieldErrorsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingRulesArchiveCreateNameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingRulesArchiveCreateDisplayNameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingRulesArchiveCreateLabelsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingRulesArchiveCreateAnnotationsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingRulesArchiveCreateDebugModeErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingRulesArchiveCreateProviderErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingRulesArchiveCreateProviderReferenceErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingRulesArchiveCreateProviderIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingRulesArchiveCreateReconciliationEnabledErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingRulesArchiveCreatePlatformServiceErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingRulesArchiveCreateKindErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingRulesArchiveCreateTolerationsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingRulesArchiveCreateArchivedErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingRulesArchiveCreateArchivedAtErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingRulesArchiveCreateArchivedReasonErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingRulesArchiveCreateCriticalityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingRulesArchiveCreateTargetAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingRulesArchiveCreateSloTargetErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingRulesArchiveCreateSloAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingRulesArchiveCreateSlaTargetErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingRulesArchiveCreateSlaAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingRulesArchiveCreateProductKindErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingRulesArchiveCreateDiscountTypeErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingRulesArchiveCreateDiscountValueErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingRulesArchiveCreateActiveFromErrorComponent):
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
        from ..models.api_v1_pricing_rules_archive_create_active_from_error_component import (
            ApiV1PricingRulesArchiveCreateActiveFromErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_rules_archive_create_active_until_error_component import (
            ApiV1PricingRulesArchiveCreateActiveUntilErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_rules_archive_create_annotations_error_component import (
            ApiV1PricingRulesArchiveCreateAnnotationsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_rules_archive_create_archived_at_error_component import (
            ApiV1PricingRulesArchiveCreateArchivedAtErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_rules_archive_create_archived_error_component import (
            ApiV1PricingRulesArchiveCreateArchivedErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_rules_archive_create_archived_reason_error_component import (
            ApiV1PricingRulesArchiveCreateArchivedReasonErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_rules_archive_create_criticality_error_component import (
            ApiV1PricingRulesArchiveCreateCriticalityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_rules_archive_create_debug_mode_error_component import (
            ApiV1PricingRulesArchiveCreateDebugModeErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_rules_archive_create_discount_type_error_component import (
            ApiV1PricingRulesArchiveCreateDiscountTypeErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_rules_archive_create_discount_value_error_component import (
            ApiV1PricingRulesArchiveCreateDiscountValueErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_rules_archive_create_display_name_error_component import (
            ApiV1PricingRulesArchiveCreateDisplayNameErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_rules_archive_create_kind_error_component import (
            ApiV1PricingRulesArchiveCreateKindErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_rules_archive_create_labels_error_component import (
            ApiV1PricingRulesArchiveCreateLabelsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_rules_archive_create_name_error_component import (
            ApiV1PricingRulesArchiveCreateNameErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_rules_archive_create_non_field_errors_error_component import (
            ApiV1PricingRulesArchiveCreateNonFieldErrorsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_rules_archive_create_platform_service_error_component import (
            ApiV1PricingRulesArchiveCreatePlatformServiceErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_rules_archive_create_product_kind_error_component import (
            ApiV1PricingRulesArchiveCreateProductKindErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_rules_archive_create_provider_error_component import (
            ApiV1PricingRulesArchiveCreateProviderErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_rules_archive_create_provider_id_error_component import (
            ApiV1PricingRulesArchiveCreateProviderIdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_rules_archive_create_provider_reference_error_component import (
            ApiV1PricingRulesArchiveCreateProviderReferenceErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_rules_archive_create_reconciliation_enabled_error_component import (
            ApiV1PricingRulesArchiveCreateReconciliationEnabledErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_rules_archive_create_sla_availability_error_component import (
            ApiV1PricingRulesArchiveCreateSlaAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_rules_archive_create_sla_target_error_component import (
            ApiV1PricingRulesArchiveCreateSlaTargetErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_rules_archive_create_slo_availability_error_component import (
            ApiV1PricingRulesArchiveCreateSloAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_rules_archive_create_slo_target_error_component import (
            ApiV1PricingRulesArchiveCreateSloTargetErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_rules_archive_create_target_availability_error_component import (
            ApiV1PricingRulesArchiveCreateTargetAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_rules_archive_create_tolerations_error_component import (
            ApiV1PricingRulesArchiveCreateTolerationsErrorComponent,  # noqa: PLC0415
        )

        d = dict(src_dict)
        type_ = check_validation_error_enum(d.pop("type"))

        errors = []
        _errors = d.pop("errors")
        for errors_item_data in _errors:

            def _parse_errors_item(
                data: object,
            ) -> (
                ApiV1PricingRulesArchiveCreateActiveFromErrorComponent
                | ApiV1PricingRulesArchiveCreateActiveUntilErrorComponent
                | ApiV1PricingRulesArchiveCreateAnnotationsErrorComponent
                | ApiV1PricingRulesArchiveCreateArchivedAtErrorComponent
                | ApiV1PricingRulesArchiveCreateArchivedErrorComponent
                | ApiV1PricingRulesArchiveCreateArchivedReasonErrorComponent
                | ApiV1PricingRulesArchiveCreateCriticalityErrorComponent
                | ApiV1PricingRulesArchiveCreateDebugModeErrorComponent
                | ApiV1PricingRulesArchiveCreateDiscountTypeErrorComponent
                | ApiV1PricingRulesArchiveCreateDiscountValueErrorComponent
                | ApiV1PricingRulesArchiveCreateDisplayNameErrorComponent
                | ApiV1PricingRulesArchiveCreateKindErrorComponent
                | ApiV1PricingRulesArchiveCreateLabelsErrorComponent
                | ApiV1PricingRulesArchiveCreateNameErrorComponent
                | ApiV1PricingRulesArchiveCreateNonFieldErrorsErrorComponent
                | ApiV1PricingRulesArchiveCreatePlatformServiceErrorComponent
                | ApiV1PricingRulesArchiveCreateProductKindErrorComponent
                | ApiV1PricingRulesArchiveCreateProviderErrorComponent
                | ApiV1PricingRulesArchiveCreateProviderIdErrorComponent
                | ApiV1PricingRulesArchiveCreateProviderReferenceErrorComponent
                | ApiV1PricingRulesArchiveCreateReconciliationEnabledErrorComponent
                | ApiV1PricingRulesArchiveCreateSlaAvailabilityErrorComponent
                | ApiV1PricingRulesArchiveCreateSlaTargetErrorComponent
                | ApiV1PricingRulesArchiveCreateSloAvailabilityErrorComponent
                | ApiV1PricingRulesArchiveCreateSloTargetErrorComponent
                | ApiV1PricingRulesArchiveCreateTargetAvailabilityErrorComponent
                | ApiV1PricingRulesArchiveCreateTolerationsErrorComponent
            ):
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_rules_archive_create_error_type_0 = (
                        ApiV1PricingRulesArchiveCreateNonFieldErrorsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_rules_archive_create_error_type_0
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_rules_archive_create_error_type_1 = (
                        ApiV1PricingRulesArchiveCreateNameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_rules_archive_create_error_type_1
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_rules_archive_create_error_type_2 = (
                        ApiV1PricingRulesArchiveCreateDisplayNameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_rules_archive_create_error_type_2
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_rules_archive_create_error_type_3 = (
                        ApiV1PricingRulesArchiveCreateLabelsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_rules_archive_create_error_type_3
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_rules_archive_create_error_type_4 = (
                        ApiV1PricingRulesArchiveCreateAnnotationsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_rules_archive_create_error_type_4
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_rules_archive_create_error_type_5 = (
                        ApiV1PricingRulesArchiveCreateDebugModeErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_rules_archive_create_error_type_5
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_rules_archive_create_error_type_6 = (
                        ApiV1PricingRulesArchiveCreateProviderErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_rules_archive_create_error_type_6
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_rules_archive_create_error_type_7 = (
                        ApiV1PricingRulesArchiveCreateProviderReferenceErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_rules_archive_create_error_type_7
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_rules_archive_create_error_type_8 = (
                        ApiV1PricingRulesArchiveCreateProviderIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_rules_archive_create_error_type_8
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_rules_archive_create_error_type_9 = (
                        ApiV1PricingRulesArchiveCreateReconciliationEnabledErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_rules_archive_create_error_type_9
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_rules_archive_create_error_type_10 = (
                        ApiV1PricingRulesArchiveCreatePlatformServiceErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_rules_archive_create_error_type_10
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_rules_archive_create_error_type_11 = (
                        ApiV1PricingRulesArchiveCreateKindErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_rules_archive_create_error_type_11
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_rules_archive_create_error_type_12 = (
                        ApiV1PricingRulesArchiveCreateTolerationsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_rules_archive_create_error_type_12
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_rules_archive_create_error_type_13 = (
                        ApiV1PricingRulesArchiveCreateArchivedErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_rules_archive_create_error_type_13
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_rules_archive_create_error_type_14 = (
                        ApiV1PricingRulesArchiveCreateArchivedAtErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_rules_archive_create_error_type_14
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_rules_archive_create_error_type_15 = (
                        ApiV1PricingRulesArchiveCreateArchivedReasonErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_rules_archive_create_error_type_15
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_rules_archive_create_error_type_16 = (
                        ApiV1PricingRulesArchiveCreateCriticalityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_rules_archive_create_error_type_16
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_rules_archive_create_error_type_17 = (
                        ApiV1PricingRulesArchiveCreateTargetAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_rules_archive_create_error_type_17
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_rules_archive_create_error_type_18 = (
                        ApiV1PricingRulesArchiveCreateSloTargetErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_rules_archive_create_error_type_18
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_rules_archive_create_error_type_19 = (
                        ApiV1PricingRulesArchiveCreateSloAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_rules_archive_create_error_type_19
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_rules_archive_create_error_type_20 = (
                        ApiV1PricingRulesArchiveCreateSlaTargetErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_rules_archive_create_error_type_20
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_rules_archive_create_error_type_21 = (
                        ApiV1PricingRulesArchiveCreateSlaAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_rules_archive_create_error_type_21
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_rules_archive_create_error_type_22 = (
                        ApiV1PricingRulesArchiveCreateProductKindErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_rules_archive_create_error_type_22
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_rules_archive_create_error_type_23 = (
                        ApiV1PricingRulesArchiveCreateDiscountTypeErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_rules_archive_create_error_type_23
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_rules_archive_create_error_type_24 = (
                        ApiV1PricingRulesArchiveCreateDiscountValueErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_rules_archive_create_error_type_24
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_rules_archive_create_error_type_25 = (
                        ApiV1PricingRulesArchiveCreateActiveFromErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_rules_archive_create_error_type_25
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_api_v1_pricing_rules_archive_create_error_type_26 = (
                    ApiV1PricingRulesArchiveCreateActiveUntilErrorComponent.from_dict(data)
                )

                return componentsschemas_api_v1_pricing_rules_archive_create_error_type_26

            errors_item = _parse_errors_item(errors_item_data)

            errors.append(errors_item)

        api_v1_pricing_rules_archive_create_validation_error = cls(
            type_=type_,
            errors=errors,
        )

        api_v1_pricing_rules_archive_create_validation_error.additional_properties = d
        return api_v1_pricing_rules_archive_create_validation_error

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
