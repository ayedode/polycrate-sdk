from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.validation_error_enum import ValidationErrorEnum, check_validation_error_enum

if TYPE_CHECKING:
    from ..models.api_v1_pricing_rules_create_active_from_error_component import (
        ApiV1PricingRulesCreateActiveFromErrorComponent,
    )
    from ..models.api_v1_pricing_rules_create_active_until_error_component import (
        ApiV1PricingRulesCreateActiveUntilErrorComponent,
    )
    from ..models.api_v1_pricing_rules_create_annotations_error_component import (
        ApiV1PricingRulesCreateAnnotationsErrorComponent,
    )
    from ..models.api_v1_pricing_rules_create_archived_at_error_component import (
        ApiV1PricingRulesCreateArchivedAtErrorComponent,
    )
    from ..models.api_v1_pricing_rules_create_archived_error_component import (
        ApiV1PricingRulesCreateArchivedErrorComponent,
    )
    from ..models.api_v1_pricing_rules_create_archived_reason_error_component import (
        ApiV1PricingRulesCreateArchivedReasonErrorComponent,
    )
    from ..models.api_v1_pricing_rules_create_criticality_error_component import (
        ApiV1PricingRulesCreateCriticalityErrorComponent,
    )
    from ..models.api_v1_pricing_rules_create_debug_mode_error_component import (
        ApiV1PricingRulesCreateDebugModeErrorComponent,
    )
    from ..models.api_v1_pricing_rules_create_discount_type_error_component import (
        ApiV1PricingRulesCreateDiscountTypeErrorComponent,
    )
    from ..models.api_v1_pricing_rules_create_discount_value_error_component import (
        ApiV1PricingRulesCreateDiscountValueErrorComponent,
    )
    from ..models.api_v1_pricing_rules_create_display_name_error_component import (
        ApiV1PricingRulesCreateDisplayNameErrorComponent,
    )
    from ..models.api_v1_pricing_rules_create_kind_error_component import ApiV1PricingRulesCreateKindErrorComponent
    from ..models.api_v1_pricing_rules_create_labels_error_component import ApiV1PricingRulesCreateLabelsErrorComponent
    from ..models.api_v1_pricing_rules_create_name_error_component import ApiV1PricingRulesCreateNameErrorComponent
    from ..models.api_v1_pricing_rules_create_non_field_errors_error_component import (
        ApiV1PricingRulesCreateNonFieldErrorsErrorComponent,
    )
    from ..models.api_v1_pricing_rules_create_platform_service_error_component import (
        ApiV1PricingRulesCreatePlatformServiceErrorComponent,
    )
    from ..models.api_v1_pricing_rules_create_product_kind_error_component import (
        ApiV1PricingRulesCreateProductKindErrorComponent,
    )
    from ..models.api_v1_pricing_rules_create_provider_error_component import (
        ApiV1PricingRulesCreateProviderErrorComponent,
    )
    from ..models.api_v1_pricing_rules_create_provider_id_error_component import (
        ApiV1PricingRulesCreateProviderIdErrorComponent,
    )
    from ..models.api_v1_pricing_rules_create_provider_reference_error_component import (
        ApiV1PricingRulesCreateProviderReferenceErrorComponent,
    )
    from ..models.api_v1_pricing_rules_create_reconciliation_enabled_error_component import (
        ApiV1PricingRulesCreateReconciliationEnabledErrorComponent,
    )
    from ..models.api_v1_pricing_rules_create_sla_availability_error_component import (
        ApiV1PricingRulesCreateSlaAvailabilityErrorComponent,
    )
    from ..models.api_v1_pricing_rules_create_sla_target_error_component import (
        ApiV1PricingRulesCreateSlaTargetErrorComponent,
    )
    from ..models.api_v1_pricing_rules_create_slo_availability_error_component import (
        ApiV1PricingRulesCreateSloAvailabilityErrorComponent,
    )
    from ..models.api_v1_pricing_rules_create_slo_target_error_component import (
        ApiV1PricingRulesCreateSloTargetErrorComponent,
    )
    from ..models.api_v1_pricing_rules_create_target_availability_error_component import (
        ApiV1PricingRulesCreateTargetAvailabilityErrorComponent,
    )
    from ..models.api_v1_pricing_rules_create_tolerations_error_component import (
        ApiV1PricingRulesCreateTolerationsErrorComponent,
    )


T = TypeVar("T", bound="ApiV1PricingRulesCreateValidationError")


@_attrs_define
class ApiV1PricingRulesCreateValidationError:
    """
    Attributes:
        type_ (ValidationErrorEnum): * `validation_error` - Validation Error
        errors (list[ApiV1PricingRulesCreateActiveFromErrorComponent | ApiV1PricingRulesCreateActiveUntilErrorComponent
            | ApiV1PricingRulesCreateAnnotationsErrorComponent | ApiV1PricingRulesCreateArchivedAtErrorComponent |
            ApiV1PricingRulesCreateArchivedErrorComponent | ApiV1PricingRulesCreateArchivedReasonErrorComponent |
            ApiV1PricingRulesCreateCriticalityErrorComponent | ApiV1PricingRulesCreateDebugModeErrorComponent |
            ApiV1PricingRulesCreateDiscountTypeErrorComponent | ApiV1PricingRulesCreateDiscountValueErrorComponent |
            ApiV1PricingRulesCreateDisplayNameErrorComponent | ApiV1PricingRulesCreateKindErrorComponent |
            ApiV1PricingRulesCreateLabelsErrorComponent | ApiV1PricingRulesCreateNameErrorComponent |
            ApiV1PricingRulesCreateNonFieldErrorsErrorComponent | ApiV1PricingRulesCreatePlatformServiceErrorComponent |
            ApiV1PricingRulesCreateProductKindErrorComponent | ApiV1PricingRulesCreateProviderErrorComponent |
            ApiV1PricingRulesCreateProviderIdErrorComponent | ApiV1PricingRulesCreateProviderReferenceErrorComponent |
            ApiV1PricingRulesCreateReconciliationEnabledErrorComponent |
            ApiV1PricingRulesCreateSlaAvailabilityErrorComponent | ApiV1PricingRulesCreateSlaTargetErrorComponent |
            ApiV1PricingRulesCreateSloAvailabilityErrorComponent | ApiV1PricingRulesCreateSloTargetErrorComponent |
            ApiV1PricingRulesCreateTargetAvailabilityErrorComponent | ApiV1PricingRulesCreateTolerationsErrorComponent]):
    """

    type_: ValidationErrorEnum
    errors: list[
        ApiV1PricingRulesCreateActiveFromErrorComponent
        | ApiV1PricingRulesCreateActiveUntilErrorComponent
        | ApiV1PricingRulesCreateAnnotationsErrorComponent
        | ApiV1PricingRulesCreateArchivedAtErrorComponent
        | ApiV1PricingRulesCreateArchivedErrorComponent
        | ApiV1PricingRulesCreateArchivedReasonErrorComponent
        | ApiV1PricingRulesCreateCriticalityErrorComponent
        | ApiV1PricingRulesCreateDebugModeErrorComponent
        | ApiV1PricingRulesCreateDiscountTypeErrorComponent
        | ApiV1PricingRulesCreateDiscountValueErrorComponent
        | ApiV1PricingRulesCreateDisplayNameErrorComponent
        | ApiV1PricingRulesCreateKindErrorComponent
        | ApiV1PricingRulesCreateLabelsErrorComponent
        | ApiV1PricingRulesCreateNameErrorComponent
        | ApiV1PricingRulesCreateNonFieldErrorsErrorComponent
        | ApiV1PricingRulesCreatePlatformServiceErrorComponent
        | ApiV1PricingRulesCreateProductKindErrorComponent
        | ApiV1PricingRulesCreateProviderErrorComponent
        | ApiV1PricingRulesCreateProviderIdErrorComponent
        | ApiV1PricingRulesCreateProviderReferenceErrorComponent
        | ApiV1PricingRulesCreateReconciliationEnabledErrorComponent
        | ApiV1PricingRulesCreateSlaAvailabilityErrorComponent
        | ApiV1PricingRulesCreateSlaTargetErrorComponent
        | ApiV1PricingRulesCreateSloAvailabilityErrorComponent
        | ApiV1PricingRulesCreateSloTargetErrorComponent
        | ApiV1PricingRulesCreateTargetAvailabilityErrorComponent
        | ApiV1PricingRulesCreateTolerationsErrorComponent
    ]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.api_v1_pricing_rules_create_active_from_error_component import (
            ApiV1PricingRulesCreateActiveFromErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_rules_create_annotations_error_component import (
            ApiV1PricingRulesCreateAnnotationsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_rules_create_archived_at_error_component import (
            ApiV1PricingRulesCreateArchivedAtErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_rules_create_archived_error_component import (
            ApiV1PricingRulesCreateArchivedErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_rules_create_archived_reason_error_component import (
            ApiV1PricingRulesCreateArchivedReasonErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_rules_create_criticality_error_component import (
            ApiV1PricingRulesCreateCriticalityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_rules_create_debug_mode_error_component import (
            ApiV1PricingRulesCreateDebugModeErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_rules_create_discount_type_error_component import (
            ApiV1PricingRulesCreateDiscountTypeErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_rules_create_discount_value_error_component import (
            ApiV1PricingRulesCreateDiscountValueErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_rules_create_display_name_error_component import (
            ApiV1PricingRulesCreateDisplayNameErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_rules_create_kind_error_component import (
            ApiV1PricingRulesCreateKindErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_rules_create_labels_error_component import (
            ApiV1PricingRulesCreateLabelsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_rules_create_name_error_component import (
            ApiV1PricingRulesCreateNameErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_rules_create_non_field_errors_error_component import (
            ApiV1PricingRulesCreateNonFieldErrorsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_rules_create_platform_service_error_component import (
            ApiV1PricingRulesCreatePlatformServiceErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_rules_create_product_kind_error_component import (
            ApiV1PricingRulesCreateProductKindErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_rules_create_provider_error_component import (
            ApiV1PricingRulesCreateProviderErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_rules_create_provider_id_error_component import (
            ApiV1PricingRulesCreateProviderIdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_rules_create_provider_reference_error_component import (
            ApiV1PricingRulesCreateProviderReferenceErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_rules_create_reconciliation_enabled_error_component import (
            ApiV1PricingRulesCreateReconciliationEnabledErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_rules_create_sla_availability_error_component import (
            ApiV1PricingRulesCreateSlaAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_rules_create_sla_target_error_component import (
            ApiV1PricingRulesCreateSlaTargetErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_rules_create_slo_availability_error_component import (
            ApiV1PricingRulesCreateSloAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_rules_create_slo_target_error_component import (
            ApiV1PricingRulesCreateSloTargetErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_rules_create_target_availability_error_component import (
            ApiV1PricingRulesCreateTargetAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_rules_create_tolerations_error_component import (
            ApiV1PricingRulesCreateTolerationsErrorComponent,  # noqa: PLC0415
        )

        type_: str = self.type_

        errors = []
        for errors_item_data in self.errors:
            errors_item: dict[str, Any]
            if isinstance(errors_item_data, ApiV1PricingRulesCreateNonFieldErrorsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingRulesCreateNameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingRulesCreateDisplayNameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingRulesCreateLabelsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingRulesCreateAnnotationsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingRulesCreateDebugModeErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingRulesCreateProviderErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingRulesCreateProviderReferenceErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingRulesCreateProviderIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingRulesCreateReconciliationEnabledErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingRulesCreatePlatformServiceErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingRulesCreateKindErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingRulesCreateTolerationsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingRulesCreateArchivedErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingRulesCreateArchivedAtErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingRulesCreateArchivedReasonErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingRulesCreateCriticalityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingRulesCreateTargetAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingRulesCreateSloTargetErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingRulesCreateSloAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingRulesCreateSlaTargetErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingRulesCreateSlaAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingRulesCreateProductKindErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingRulesCreateDiscountTypeErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingRulesCreateDiscountValueErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingRulesCreateActiveFromErrorComponent):
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
        from ..models.api_v1_pricing_rules_create_active_from_error_component import (
            ApiV1PricingRulesCreateActiveFromErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_rules_create_active_until_error_component import (
            ApiV1PricingRulesCreateActiveUntilErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_rules_create_annotations_error_component import (
            ApiV1PricingRulesCreateAnnotationsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_rules_create_archived_at_error_component import (
            ApiV1PricingRulesCreateArchivedAtErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_rules_create_archived_error_component import (
            ApiV1PricingRulesCreateArchivedErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_rules_create_archived_reason_error_component import (
            ApiV1PricingRulesCreateArchivedReasonErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_rules_create_criticality_error_component import (
            ApiV1PricingRulesCreateCriticalityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_rules_create_debug_mode_error_component import (
            ApiV1PricingRulesCreateDebugModeErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_rules_create_discount_type_error_component import (
            ApiV1PricingRulesCreateDiscountTypeErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_rules_create_discount_value_error_component import (
            ApiV1PricingRulesCreateDiscountValueErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_rules_create_display_name_error_component import (
            ApiV1PricingRulesCreateDisplayNameErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_rules_create_kind_error_component import (
            ApiV1PricingRulesCreateKindErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_rules_create_labels_error_component import (
            ApiV1PricingRulesCreateLabelsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_rules_create_name_error_component import (
            ApiV1PricingRulesCreateNameErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_rules_create_non_field_errors_error_component import (
            ApiV1PricingRulesCreateNonFieldErrorsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_rules_create_platform_service_error_component import (
            ApiV1PricingRulesCreatePlatformServiceErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_rules_create_product_kind_error_component import (
            ApiV1PricingRulesCreateProductKindErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_rules_create_provider_error_component import (
            ApiV1PricingRulesCreateProviderErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_rules_create_provider_id_error_component import (
            ApiV1PricingRulesCreateProviderIdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_rules_create_provider_reference_error_component import (
            ApiV1PricingRulesCreateProviderReferenceErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_rules_create_reconciliation_enabled_error_component import (
            ApiV1PricingRulesCreateReconciliationEnabledErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_rules_create_sla_availability_error_component import (
            ApiV1PricingRulesCreateSlaAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_rules_create_sla_target_error_component import (
            ApiV1PricingRulesCreateSlaTargetErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_rules_create_slo_availability_error_component import (
            ApiV1PricingRulesCreateSloAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_rules_create_slo_target_error_component import (
            ApiV1PricingRulesCreateSloTargetErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_rules_create_target_availability_error_component import (
            ApiV1PricingRulesCreateTargetAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_rules_create_tolerations_error_component import (
            ApiV1PricingRulesCreateTolerationsErrorComponent,  # noqa: PLC0415
        )

        d = dict(src_dict)
        type_ = check_validation_error_enum(d.pop("type"))

        errors = []
        _errors = d.pop("errors")
        for errors_item_data in _errors:

            def _parse_errors_item(
                data: object,
            ) -> (
                ApiV1PricingRulesCreateActiveFromErrorComponent
                | ApiV1PricingRulesCreateActiveUntilErrorComponent
                | ApiV1PricingRulesCreateAnnotationsErrorComponent
                | ApiV1PricingRulesCreateArchivedAtErrorComponent
                | ApiV1PricingRulesCreateArchivedErrorComponent
                | ApiV1PricingRulesCreateArchivedReasonErrorComponent
                | ApiV1PricingRulesCreateCriticalityErrorComponent
                | ApiV1PricingRulesCreateDebugModeErrorComponent
                | ApiV1PricingRulesCreateDiscountTypeErrorComponent
                | ApiV1PricingRulesCreateDiscountValueErrorComponent
                | ApiV1PricingRulesCreateDisplayNameErrorComponent
                | ApiV1PricingRulesCreateKindErrorComponent
                | ApiV1PricingRulesCreateLabelsErrorComponent
                | ApiV1PricingRulesCreateNameErrorComponent
                | ApiV1PricingRulesCreateNonFieldErrorsErrorComponent
                | ApiV1PricingRulesCreatePlatformServiceErrorComponent
                | ApiV1PricingRulesCreateProductKindErrorComponent
                | ApiV1PricingRulesCreateProviderErrorComponent
                | ApiV1PricingRulesCreateProviderIdErrorComponent
                | ApiV1PricingRulesCreateProviderReferenceErrorComponent
                | ApiV1PricingRulesCreateReconciliationEnabledErrorComponent
                | ApiV1PricingRulesCreateSlaAvailabilityErrorComponent
                | ApiV1PricingRulesCreateSlaTargetErrorComponent
                | ApiV1PricingRulesCreateSloAvailabilityErrorComponent
                | ApiV1PricingRulesCreateSloTargetErrorComponent
                | ApiV1PricingRulesCreateTargetAvailabilityErrorComponent
                | ApiV1PricingRulesCreateTolerationsErrorComponent
            ):
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_rules_create_error_type_0 = (
                        ApiV1PricingRulesCreateNonFieldErrorsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_rules_create_error_type_0
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_rules_create_error_type_1 = (
                        ApiV1PricingRulesCreateNameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_rules_create_error_type_1
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_rules_create_error_type_2 = (
                        ApiV1PricingRulesCreateDisplayNameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_rules_create_error_type_2
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_rules_create_error_type_3 = (
                        ApiV1PricingRulesCreateLabelsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_rules_create_error_type_3
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_rules_create_error_type_4 = (
                        ApiV1PricingRulesCreateAnnotationsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_rules_create_error_type_4
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_rules_create_error_type_5 = (
                        ApiV1PricingRulesCreateDebugModeErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_rules_create_error_type_5
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_rules_create_error_type_6 = (
                        ApiV1PricingRulesCreateProviderErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_rules_create_error_type_6
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_rules_create_error_type_7 = (
                        ApiV1PricingRulesCreateProviderReferenceErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_rules_create_error_type_7
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_rules_create_error_type_8 = (
                        ApiV1PricingRulesCreateProviderIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_rules_create_error_type_8
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_rules_create_error_type_9 = (
                        ApiV1PricingRulesCreateReconciliationEnabledErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_rules_create_error_type_9
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_rules_create_error_type_10 = (
                        ApiV1PricingRulesCreatePlatformServiceErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_rules_create_error_type_10
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_rules_create_error_type_11 = (
                        ApiV1PricingRulesCreateKindErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_rules_create_error_type_11
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_rules_create_error_type_12 = (
                        ApiV1PricingRulesCreateTolerationsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_rules_create_error_type_12
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_rules_create_error_type_13 = (
                        ApiV1PricingRulesCreateArchivedErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_rules_create_error_type_13
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_rules_create_error_type_14 = (
                        ApiV1PricingRulesCreateArchivedAtErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_rules_create_error_type_14
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_rules_create_error_type_15 = (
                        ApiV1PricingRulesCreateArchivedReasonErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_rules_create_error_type_15
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_rules_create_error_type_16 = (
                        ApiV1PricingRulesCreateCriticalityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_rules_create_error_type_16
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_rules_create_error_type_17 = (
                        ApiV1PricingRulesCreateTargetAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_rules_create_error_type_17
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_rules_create_error_type_18 = (
                        ApiV1PricingRulesCreateSloTargetErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_rules_create_error_type_18
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_rules_create_error_type_19 = (
                        ApiV1PricingRulesCreateSloAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_rules_create_error_type_19
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_rules_create_error_type_20 = (
                        ApiV1PricingRulesCreateSlaTargetErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_rules_create_error_type_20
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_rules_create_error_type_21 = (
                        ApiV1PricingRulesCreateSlaAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_rules_create_error_type_21
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_rules_create_error_type_22 = (
                        ApiV1PricingRulesCreateProductKindErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_rules_create_error_type_22
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_rules_create_error_type_23 = (
                        ApiV1PricingRulesCreateDiscountTypeErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_rules_create_error_type_23
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_rules_create_error_type_24 = (
                        ApiV1PricingRulesCreateDiscountValueErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_rules_create_error_type_24
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_rules_create_error_type_25 = (
                        ApiV1PricingRulesCreateActiveFromErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_rules_create_error_type_25
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_api_v1_pricing_rules_create_error_type_26 = (
                    ApiV1PricingRulesCreateActiveUntilErrorComponent.from_dict(data)
                )

                return componentsschemas_api_v1_pricing_rules_create_error_type_26

            errors_item = _parse_errors_item(errors_item_data)

            errors.append(errors_item)

        api_v1_pricing_rules_create_validation_error = cls(
            type_=type_,
            errors=errors,
        )

        api_v1_pricing_rules_create_validation_error.additional_properties = d
        return api_v1_pricing_rules_create_validation_error

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
