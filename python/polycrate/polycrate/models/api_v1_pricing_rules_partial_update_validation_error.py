from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.validation_error_enum import ValidationErrorEnum, check_validation_error_enum

if TYPE_CHECKING:
    from ..models.api_v1_pricing_rules_partial_update_active_from_error_component import (
        ApiV1PricingRulesPartialUpdateActiveFromErrorComponent,
    )
    from ..models.api_v1_pricing_rules_partial_update_active_until_error_component import (
        ApiV1PricingRulesPartialUpdateActiveUntilErrorComponent,
    )
    from ..models.api_v1_pricing_rules_partial_update_annotations_error_component import (
        ApiV1PricingRulesPartialUpdateAnnotationsErrorComponent,
    )
    from ..models.api_v1_pricing_rules_partial_update_archived_at_error_component import (
        ApiV1PricingRulesPartialUpdateArchivedAtErrorComponent,
    )
    from ..models.api_v1_pricing_rules_partial_update_archived_error_component import (
        ApiV1PricingRulesPartialUpdateArchivedErrorComponent,
    )
    from ..models.api_v1_pricing_rules_partial_update_archived_reason_error_component import (
        ApiV1PricingRulesPartialUpdateArchivedReasonErrorComponent,
    )
    from ..models.api_v1_pricing_rules_partial_update_criticality_error_component import (
        ApiV1PricingRulesPartialUpdateCriticalityErrorComponent,
    )
    from ..models.api_v1_pricing_rules_partial_update_debug_mode_error_component import (
        ApiV1PricingRulesPartialUpdateDebugModeErrorComponent,
    )
    from ..models.api_v1_pricing_rules_partial_update_discount_type_error_component import (
        ApiV1PricingRulesPartialUpdateDiscountTypeErrorComponent,
    )
    from ..models.api_v1_pricing_rules_partial_update_discount_value_error_component import (
        ApiV1PricingRulesPartialUpdateDiscountValueErrorComponent,
    )
    from ..models.api_v1_pricing_rules_partial_update_display_name_error_component import (
        ApiV1PricingRulesPartialUpdateDisplayNameErrorComponent,
    )
    from ..models.api_v1_pricing_rules_partial_update_kind_error_component import (
        ApiV1PricingRulesPartialUpdateKindErrorComponent,
    )
    from ..models.api_v1_pricing_rules_partial_update_labels_error_component import (
        ApiV1PricingRulesPartialUpdateLabelsErrorComponent,
    )
    from ..models.api_v1_pricing_rules_partial_update_name_error_component import (
        ApiV1PricingRulesPartialUpdateNameErrorComponent,
    )
    from ..models.api_v1_pricing_rules_partial_update_non_field_errors_error_component import (
        ApiV1PricingRulesPartialUpdateNonFieldErrorsErrorComponent,
    )
    from ..models.api_v1_pricing_rules_partial_update_platform_service_error_component import (
        ApiV1PricingRulesPartialUpdatePlatformServiceErrorComponent,
    )
    from ..models.api_v1_pricing_rules_partial_update_product_kind_error_component import (
        ApiV1PricingRulesPartialUpdateProductKindErrorComponent,
    )
    from ..models.api_v1_pricing_rules_partial_update_provider_error_component import (
        ApiV1PricingRulesPartialUpdateProviderErrorComponent,
    )
    from ..models.api_v1_pricing_rules_partial_update_provider_id_error_component import (
        ApiV1PricingRulesPartialUpdateProviderIdErrorComponent,
    )
    from ..models.api_v1_pricing_rules_partial_update_provider_reference_error_component import (
        ApiV1PricingRulesPartialUpdateProviderReferenceErrorComponent,
    )
    from ..models.api_v1_pricing_rules_partial_update_reconciliation_enabled_error_component import (
        ApiV1PricingRulesPartialUpdateReconciliationEnabledErrorComponent,
    )
    from ..models.api_v1_pricing_rules_partial_update_sla_availability_error_component import (
        ApiV1PricingRulesPartialUpdateSlaAvailabilityErrorComponent,
    )
    from ..models.api_v1_pricing_rules_partial_update_sla_target_error_component import (
        ApiV1PricingRulesPartialUpdateSlaTargetErrorComponent,
    )
    from ..models.api_v1_pricing_rules_partial_update_slo_availability_error_component import (
        ApiV1PricingRulesPartialUpdateSloAvailabilityErrorComponent,
    )
    from ..models.api_v1_pricing_rules_partial_update_slo_target_error_component import (
        ApiV1PricingRulesPartialUpdateSloTargetErrorComponent,
    )
    from ..models.api_v1_pricing_rules_partial_update_target_availability_error_component import (
        ApiV1PricingRulesPartialUpdateTargetAvailabilityErrorComponent,
    )
    from ..models.api_v1_pricing_rules_partial_update_tolerations_error_component import (
        ApiV1PricingRulesPartialUpdateTolerationsErrorComponent,
    )


T = TypeVar("T", bound="ApiV1PricingRulesPartialUpdateValidationError")


@_attrs_define
class ApiV1PricingRulesPartialUpdateValidationError:
    """
    Attributes:
        type_ (ValidationErrorEnum): * `validation_error` - Validation Error
        errors (list[ApiV1PricingRulesPartialUpdateActiveFromErrorComponent |
            ApiV1PricingRulesPartialUpdateActiveUntilErrorComponent |
            ApiV1PricingRulesPartialUpdateAnnotationsErrorComponent | ApiV1PricingRulesPartialUpdateArchivedAtErrorComponent
            | ApiV1PricingRulesPartialUpdateArchivedErrorComponent |
            ApiV1PricingRulesPartialUpdateArchivedReasonErrorComponent |
            ApiV1PricingRulesPartialUpdateCriticalityErrorComponent | ApiV1PricingRulesPartialUpdateDebugModeErrorComponent
            | ApiV1PricingRulesPartialUpdateDiscountTypeErrorComponent |
            ApiV1PricingRulesPartialUpdateDiscountValueErrorComponent |
            ApiV1PricingRulesPartialUpdateDisplayNameErrorComponent | ApiV1PricingRulesPartialUpdateKindErrorComponent |
            ApiV1PricingRulesPartialUpdateLabelsErrorComponent | ApiV1PricingRulesPartialUpdateNameErrorComponent |
            ApiV1PricingRulesPartialUpdateNonFieldErrorsErrorComponent |
            ApiV1PricingRulesPartialUpdatePlatformServiceErrorComponent |
            ApiV1PricingRulesPartialUpdateProductKindErrorComponent | ApiV1PricingRulesPartialUpdateProviderErrorComponent |
            ApiV1PricingRulesPartialUpdateProviderIdErrorComponent |
            ApiV1PricingRulesPartialUpdateProviderReferenceErrorComponent |
            ApiV1PricingRulesPartialUpdateReconciliationEnabledErrorComponent |
            ApiV1PricingRulesPartialUpdateSlaAvailabilityErrorComponent |
            ApiV1PricingRulesPartialUpdateSlaTargetErrorComponent |
            ApiV1PricingRulesPartialUpdateSloAvailabilityErrorComponent |
            ApiV1PricingRulesPartialUpdateSloTargetErrorComponent |
            ApiV1PricingRulesPartialUpdateTargetAvailabilityErrorComponent |
            ApiV1PricingRulesPartialUpdateTolerationsErrorComponent]):
    """

    type_: ValidationErrorEnum
    errors: list[
        ApiV1PricingRulesPartialUpdateActiveFromErrorComponent
        | ApiV1PricingRulesPartialUpdateActiveUntilErrorComponent
        | ApiV1PricingRulesPartialUpdateAnnotationsErrorComponent
        | ApiV1PricingRulesPartialUpdateArchivedAtErrorComponent
        | ApiV1PricingRulesPartialUpdateArchivedErrorComponent
        | ApiV1PricingRulesPartialUpdateArchivedReasonErrorComponent
        | ApiV1PricingRulesPartialUpdateCriticalityErrorComponent
        | ApiV1PricingRulesPartialUpdateDebugModeErrorComponent
        | ApiV1PricingRulesPartialUpdateDiscountTypeErrorComponent
        | ApiV1PricingRulesPartialUpdateDiscountValueErrorComponent
        | ApiV1PricingRulesPartialUpdateDisplayNameErrorComponent
        | ApiV1PricingRulesPartialUpdateKindErrorComponent
        | ApiV1PricingRulesPartialUpdateLabelsErrorComponent
        | ApiV1PricingRulesPartialUpdateNameErrorComponent
        | ApiV1PricingRulesPartialUpdateNonFieldErrorsErrorComponent
        | ApiV1PricingRulesPartialUpdatePlatformServiceErrorComponent
        | ApiV1PricingRulesPartialUpdateProductKindErrorComponent
        | ApiV1PricingRulesPartialUpdateProviderErrorComponent
        | ApiV1PricingRulesPartialUpdateProviderIdErrorComponent
        | ApiV1PricingRulesPartialUpdateProviderReferenceErrorComponent
        | ApiV1PricingRulesPartialUpdateReconciliationEnabledErrorComponent
        | ApiV1PricingRulesPartialUpdateSlaAvailabilityErrorComponent
        | ApiV1PricingRulesPartialUpdateSlaTargetErrorComponent
        | ApiV1PricingRulesPartialUpdateSloAvailabilityErrorComponent
        | ApiV1PricingRulesPartialUpdateSloTargetErrorComponent
        | ApiV1PricingRulesPartialUpdateTargetAvailabilityErrorComponent
        | ApiV1PricingRulesPartialUpdateTolerationsErrorComponent
    ]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.api_v1_pricing_rules_partial_update_active_from_error_component import (
            ApiV1PricingRulesPartialUpdateActiveFromErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_rules_partial_update_annotations_error_component import (
            ApiV1PricingRulesPartialUpdateAnnotationsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_rules_partial_update_archived_at_error_component import (
            ApiV1PricingRulesPartialUpdateArchivedAtErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_rules_partial_update_archived_error_component import (
            ApiV1PricingRulesPartialUpdateArchivedErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_rules_partial_update_archived_reason_error_component import (
            ApiV1PricingRulesPartialUpdateArchivedReasonErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_rules_partial_update_criticality_error_component import (
            ApiV1PricingRulesPartialUpdateCriticalityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_rules_partial_update_debug_mode_error_component import (
            ApiV1PricingRulesPartialUpdateDebugModeErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_rules_partial_update_discount_type_error_component import (
            ApiV1PricingRulesPartialUpdateDiscountTypeErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_rules_partial_update_discount_value_error_component import (
            ApiV1PricingRulesPartialUpdateDiscountValueErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_rules_partial_update_display_name_error_component import (
            ApiV1PricingRulesPartialUpdateDisplayNameErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_rules_partial_update_kind_error_component import (
            ApiV1PricingRulesPartialUpdateKindErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_rules_partial_update_labels_error_component import (
            ApiV1PricingRulesPartialUpdateLabelsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_rules_partial_update_name_error_component import (
            ApiV1PricingRulesPartialUpdateNameErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_rules_partial_update_non_field_errors_error_component import (
            ApiV1PricingRulesPartialUpdateNonFieldErrorsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_rules_partial_update_platform_service_error_component import (
            ApiV1PricingRulesPartialUpdatePlatformServiceErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_rules_partial_update_product_kind_error_component import (
            ApiV1PricingRulesPartialUpdateProductKindErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_rules_partial_update_provider_error_component import (
            ApiV1PricingRulesPartialUpdateProviderErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_rules_partial_update_provider_id_error_component import (
            ApiV1PricingRulesPartialUpdateProviderIdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_rules_partial_update_provider_reference_error_component import (
            ApiV1PricingRulesPartialUpdateProviderReferenceErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_rules_partial_update_reconciliation_enabled_error_component import (
            ApiV1PricingRulesPartialUpdateReconciliationEnabledErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_rules_partial_update_sla_availability_error_component import (
            ApiV1PricingRulesPartialUpdateSlaAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_rules_partial_update_sla_target_error_component import (
            ApiV1PricingRulesPartialUpdateSlaTargetErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_rules_partial_update_slo_availability_error_component import (
            ApiV1PricingRulesPartialUpdateSloAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_rules_partial_update_slo_target_error_component import (
            ApiV1PricingRulesPartialUpdateSloTargetErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_rules_partial_update_target_availability_error_component import (
            ApiV1PricingRulesPartialUpdateTargetAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_rules_partial_update_tolerations_error_component import (
            ApiV1PricingRulesPartialUpdateTolerationsErrorComponent,  # noqa: PLC0415
        )

        type_: str = self.type_

        errors = []
        for errors_item_data in self.errors:
            errors_item: dict[str, Any]
            if isinstance(errors_item_data, ApiV1PricingRulesPartialUpdateNonFieldErrorsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingRulesPartialUpdateNameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingRulesPartialUpdateDisplayNameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingRulesPartialUpdateLabelsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingRulesPartialUpdateAnnotationsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingRulesPartialUpdateDebugModeErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingRulesPartialUpdateProviderErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingRulesPartialUpdateProviderReferenceErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingRulesPartialUpdateProviderIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingRulesPartialUpdateReconciliationEnabledErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingRulesPartialUpdatePlatformServiceErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingRulesPartialUpdateKindErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingRulesPartialUpdateTolerationsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingRulesPartialUpdateArchivedErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingRulesPartialUpdateArchivedAtErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingRulesPartialUpdateArchivedReasonErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingRulesPartialUpdateCriticalityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingRulesPartialUpdateTargetAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingRulesPartialUpdateSloTargetErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingRulesPartialUpdateSloAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingRulesPartialUpdateSlaTargetErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingRulesPartialUpdateSlaAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingRulesPartialUpdateProductKindErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingRulesPartialUpdateDiscountTypeErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingRulesPartialUpdateDiscountValueErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingRulesPartialUpdateActiveFromErrorComponent):
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
        from ..models.api_v1_pricing_rules_partial_update_active_from_error_component import (
            ApiV1PricingRulesPartialUpdateActiveFromErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_rules_partial_update_active_until_error_component import (
            ApiV1PricingRulesPartialUpdateActiveUntilErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_rules_partial_update_annotations_error_component import (
            ApiV1PricingRulesPartialUpdateAnnotationsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_rules_partial_update_archived_at_error_component import (
            ApiV1PricingRulesPartialUpdateArchivedAtErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_rules_partial_update_archived_error_component import (
            ApiV1PricingRulesPartialUpdateArchivedErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_rules_partial_update_archived_reason_error_component import (
            ApiV1PricingRulesPartialUpdateArchivedReasonErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_rules_partial_update_criticality_error_component import (
            ApiV1PricingRulesPartialUpdateCriticalityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_rules_partial_update_debug_mode_error_component import (
            ApiV1PricingRulesPartialUpdateDebugModeErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_rules_partial_update_discount_type_error_component import (
            ApiV1PricingRulesPartialUpdateDiscountTypeErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_rules_partial_update_discount_value_error_component import (
            ApiV1PricingRulesPartialUpdateDiscountValueErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_rules_partial_update_display_name_error_component import (
            ApiV1PricingRulesPartialUpdateDisplayNameErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_rules_partial_update_kind_error_component import (
            ApiV1PricingRulesPartialUpdateKindErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_rules_partial_update_labels_error_component import (
            ApiV1PricingRulesPartialUpdateLabelsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_rules_partial_update_name_error_component import (
            ApiV1PricingRulesPartialUpdateNameErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_rules_partial_update_non_field_errors_error_component import (
            ApiV1PricingRulesPartialUpdateNonFieldErrorsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_rules_partial_update_platform_service_error_component import (
            ApiV1PricingRulesPartialUpdatePlatformServiceErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_rules_partial_update_product_kind_error_component import (
            ApiV1PricingRulesPartialUpdateProductKindErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_rules_partial_update_provider_error_component import (
            ApiV1PricingRulesPartialUpdateProviderErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_rules_partial_update_provider_id_error_component import (
            ApiV1PricingRulesPartialUpdateProviderIdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_rules_partial_update_provider_reference_error_component import (
            ApiV1PricingRulesPartialUpdateProviderReferenceErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_rules_partial_update_reconciliation_enabled_error_component import (
            ApiV1PricingRulesPartialUpdateReconciliationEnabledErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_rules_partial_update_sla_availability_error_component import (
            ApiV1PricingRulesPartialUpdateSlaAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_rules_partial_update_sla_target_error_component import (
            ApiV1PricingRulesPartialUpdateSlaTargetErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_rules_partial_update_slo_availability_error_component import (
            ApiV1PricingRulesPartialUpdateSloAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_rules_partial_update_slo_target_error_component import (
            ApiV1PricingRulesPartialUpdateSloTargetErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_rules_partial_update_target_availability_error_component import (
            ApiV1PricingRulesPartialUpdateTargetAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_rules_partial_update_tolerations_error_component import (
            ApiV1PricingRulesPartialUpdateTolerationsErrorComponent,  # noqa: PLC0415
        )

        d = dict(src_dict)
        type_ = check_validation_error_enum(d.pop("type"))

        errors = []
        _errors = d.pop("errors")
        for errors_item_data in _errors:

            def _parse_errors_item(
                data: object,
            ) -> (
                ApiV1PricingRulesPartialUpdateActiveFromErrorComponent
                | ApiV1PricingRulesPartialUpdateActiveUntilErrorComponent
                | ApiV1PricingRulesPartialUpdateAnnotationsErrorComponent
                | ApiV1PricingRulesPartialUpdateArchivedAtErrorComponent
                | ApiV1PricingRulesPartialUpdateArchivedErrorComponent
                | ApiV1PricingRulesPartialUpdateArchivedReasonErrorComponent
                | ApiV1PricingRulesPartialUpdateCriticalityErrorComponent
                | ApiV1PricingRulesPartialUpdateDebugModeErrorComponent
                | ApiV1PricingRulesPartialUpdateDiscountTypeErrorComponent
                | ApiV1PricingRulesPartialUpdateDiscountValueErrorComponent
                | ApiV1PricingRulesPartialUpdateDisplayNameErrorComponent
                | ApiV1PricingRulesPartialUpdateKindErrorComponent
                | ApiV1PricingRulesPartialUpdateLabelsErrorComponent
                | ApiV1PricingRulesPartialUpdateNameErrorComponent
                | ApiV1PricingRulesPartialUpdateNonFieldErrorsErrorComponent
                | ApiV1PricingRulesPartialUpdatePlatformServiceErrorComponent
                | ApiV1PricingRulesPartialUpdateProductKindErrorComponent
                | ApiV1PricingRulesPartialUpdateProviderErrorComponent
                | ApiV1PricingRulesPartialUpdateProviderIdErrorComponent
                | ApiV1PricingRulesPartialUpdateProviderReferenceErrorComponent
                | ApiV1PricingRulesPartialUpdateReconciliationEnabledErrorComponent
                | ApiV1PricingRulesPartialUpdateSlaAvailabilityErrorComponent
                | ApiV1PricingRulesPartialUpdateSlaTargetErrorComponent
                | ApiV1PricingRulesPartialUpdateSloAvailabilityErrorComponent
                | ApiV1PricingRulesPartialUpdateSloTargetErrorComponent
                | ApiV1PricingRulesPartialUpdateTargetAvailabilityErrorComponent
                | ApiV1PricingRulesPartialUpdateTolerationsErrorComponent
            ):
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_rules_partial_update_error_type_0 = (
                        ApiV1PricingRulesPartialUpdateNonFieldErrorsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_rules_partial_update_error_type_0
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_rules_partial_update_error_type_1 = (
                        ApiV1PricingRulesPartialUpdateNameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_rules_partial_update_error_type_1
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_rules_partial_update_error_type_2 = (
                        ApiV1PricingRulesPartialUpdateDisplayNameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_rules_partial_update_error_type_2
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_rules_partial_update_error_type_3 = (
                        ApiV1PricingRulesPartialUpdateLabelsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_rules_partial_update_error_type_3
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_rules_partial_update_error_type_4 = (
                        ApiV1PricingRulesPartialUpdateAnnotationsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_rules_partial_update_error_type_4
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_rules_partial_update_error_type_5 = (
                        ApiV1PricingRulesPartialUpdateDebugModeErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_rules_partial_update_error_type_5
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_rules_partial_update_error_type_6 = (
                        ApiV1PricingRulesPartialUpdateProviderErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_rules_partial_update_error_type_6
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_rules_partial_update_error_type_7 = (
                        ApiV1PricingRulesPartialUpdateProviderReferenceErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_rules_partial_update_error_type_7
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_rules_partial_update_error_type_8 = (
                        ApiV1PricingRulesPartialUpdateProviderIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_rules_partial_update_error_type_8
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_rules_partial_update_error_type_9 = (
                        ApiV1PricingRulesPartialUpdateReconciliationEnabledErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_rules_partial_update_error_type_9
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_rules_partial_update_error_type_10 = (
                        ApiV1PricingRulesPartialUpdatePlatformServiceErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_rules_partial_update_error_type_10
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_rules_partial_update_error_type_11 = (
                        ApiV1PricingRulesPartialUpdateKindErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_rules_partial_update_error_type_11
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_rules_partial_update_error_type_12 = (
                        ApiV1PricingRulesPartialUpdateTolerationsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_rules_partial_update_error_type_12
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_rules_partial_update_error_type_13 = (
                        ApiV1PricingRulesPartialUpdateArchivedErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_rules_partial_update_error_type_13
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_rules_partial_update_error_type_14 = (
                        ApiV1PricingRulesPartialUpdateArchivedAtErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_rules_partial_update_error_type_14
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_rules_partial_update_error_type_15 = (
                        ApiV1PricingRulesPartialUpdateArchivedReasonErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_rules_partial_update_error_type_15
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_rules_partial_update_error_type_16 = (
                        ApiV1PricingRulesPartialUpdateCriticalityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_rules_partial_update_error_type_16
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_rules_partial_update_error_type_17 = (
                        ApiV1PricingRulesPartialUpdateTargetAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_rules_partial_update_error_type_17
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_rules_partial_update_error_type_18 = (
                        ApiV1PricingRulesPartialUpdateSloTargetErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_rules_partial_update_error_type_18
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_rules_partial_update_error_type_19 = (
                        ApiV1PricingRulesPartialUpdateSloAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_rules_partial_update_error_type_19
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_rules_partial_update_error_type_20 = (
                        ApiV1PricingRulesPartialUpdateSlaTargetErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_rules_partial_update_error_type_20
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_rules_partial_update_error_type_21 = (
                        ApiV1PricingRulesPartialUpdateSlaAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_rules_partial_update_error_type_21
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_rules_partial_update_error_type_22 = (
                        ApiV1PricingRulesPartialUpdateProductKindErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_rules_partial_update_error_type_22
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_rules_partial_update_error_type_23 = (
                        ApiV1PricingRulesPartialUpdateDiscountTypeErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_rules_partial_update_error_type_23
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_rules_partial_update_error_type_24 = (
                        ApiV1PricingRulesPartialUpdateDiscountValueErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_rules_partial_update_error_type_24
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_rules_partial_update_error_type_25 = (
                        ApiV1PricingRulesPartialUpdateActiveFromErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_rules_partial_update_error_type_25
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_api_v1_pricing_rules_partial_update_error_type_26 = (
                    ApiV1PricingRulesPartialUpdateActiveUntilErrorComponent.from_dict(data)
                )

                return componentsschemas_api_v1_pricing_rules_partial_update_error_type_26

            errors_item = _parse_errors_item(errors_item_data)

            errors.append(errors_item)

        api_v1_pricing_rules_partial_update_validation_error = cls(
            type_=type_,
            errors=errors,
        )

        api_v1_pricing_rules_partial_update_validation_error.additional_properties = d
        return api_v1_pricing_rules_partial_update_validation_error

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
