from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.validation_error_enum import ValidationErrorEnum, check_validation_error_enum

if TYPE_CHECKING:
    from ..models.api_v1_pricing_rules_update_active_from_error_component import (
        ApiV1PricingRulesUpdateActiveFromErrorComponent,
    )
    from ..models.api_v1_pricing_rules_update_active_until_error_component import (
        ApiV1PricingRulesUpdateActiveUntilErrorComponent,
    )
    from ..models.api_v1_pricing_rules_update_annotations_error_component import (
        ApiV1PricingRulesUpdateAnnotationsErrorComponent,
    )
    from ..models.api_v1_pricing_rules_update_archived_at_error_component import (
        ApiV1PricingRulesUpdateArchivedAtErrorComponent,
    )
    from ..models.api_v1_pricing_rules_update_archived_error_component import (
        ApiV1PricingRulesUpdateArchivedErrorComponent,
    )
    from ..models.api_v1_pricing_rules_update_archived_reason_error_component import (
        ApiV1PricingRulesUpdateArchivedReasonErrorComponent,
    )
    from ..models.api_v1_pricing_rules_update_criticality_error_component import (
        ApiV1PricingRulesUpdateCriticalityErrorComponent,
    )
    from ..models.api_v1_pricing_rules_update_debug_mode_error_component import (
        ApiV1PricingRulesUpdateDebugModeErrorComponent,
    )
    from ..models.api_v1_pricing_rules_update_discount_type_error_component import (
        ApiV1PricingRulesUpdateDiscountTypeErrorComponent,
    )
    from ..models.api_v1_pricing_rules_update_discount_value_error_component import (
        ApiV1PricingRulesUpdateDiscountValueErrorComponent,
    )
    from ..models.api_v1_pricing_rules_update_display_name_error_component import (
        ApiV1PricingRulesUpdateDisplayNameErrorComponent,
    )
    from ..models.api_v1_pricing_rules_update_kind_error_component import ApiV1PricingRulesUpdateKindErrorComponent
    from ..models.api_v1_pricing_rules_update_labels_error_component import ApiV1PricingRulesUpdateLabelsErrorComponent
    from ..models.api_v1_pricing_rules_update_name_error_component import ApiV1PricingRulesUpdateNameErrorComponent
    from ..models.api_v1_pricing_rules_update_non_field_errors_error_component import (
        ApiV1PricingRulesUpdateNonFieldErrorsErrorComponent,
    )
    from ..models.api_v1_pricing_rules_update_platform_service_error_component import (
        ApiV1PricingRulesUpdatePlatformServiceErrorComponent,
    )
    from ..models.api_v1_pricing_rules_update_product_kind_error_component import (
        ApiV1PricingRulesUpdateProductKindErrorComponent,
    )
    from ..models.api_v1_pricing_rules_update_provider_error_component import (
        ApiV1PricingRulesUpdateProviderErrorComponent,
    )
    from ..models.api_v1_pricing_rules_update_provider_id_error_component import (
        ApiV1PricingRulesUpdateProviderIdErrorComponent,
    )
    from ..models.api_v1_pricing_rules_update_provider_reference_error_component import (
        ApiV1PricingRulesUpdateProviderReferenceErrorComponent,
    )
    from ..models.api_v1_pricing_rules_update_reconciliation_enabled_error_component import (
        ApiV1PricingRulesUpdateReconciliationEnabledErrorComponent,
    )
    from ..models.api_v1_pricing_rules_update_sla_availability_error_component import (
        ApiV1PricingRulesUpdateSlaAvailabilityErrorComponent,
    )
    from ..models.api_v1_pricing_rules_update_sla_target_error_component import (
        ApiV1PricingRulesUpdateSlaTargetErrorComponent,
    )
    from ..models.api_v1_pricing_rules_update_slo_availability_error_component import (
        ApiV1PricingRulesUpdateSloAvailabilityErrorComponent,
    )
    from ..models.api_v1_pricing_rules_update_slo_target_error_component import (
        ApiV1PricingRulesUpdateSloTargetErrorComponent,
    )
    from ..models.api_v1_pricing_rules_update_target_availability_error_component import (
        ApiV1PricingRulesUpdateTargetAvailabilityErrorComponent,
    )
    from ..models.api_v1_pricing_rules_update_tolerations_error_component import (
        ApiV1PricingRulesUpdateTolerationsErrorComponent,
    )


T = TypeVar("T", bound="ApiV1PricingRulesUpdateValidationError")


@_attrs_define
class ApiV1PricingRulesUpdateValidationError:
    """
    Attributes:
        type_ (ValidationErrorEnum): * `validation_error` - Validation Error
        errors (list[ApiV1PricingRulesUpdateActiveFromErrorComponent | ApiV1PricingRulesUpdateActiveUntilErrorComponent
            | ApiV1PricingRulesUpdateAnnotationsErrorComponent | ApiV1PricingRulesUpdateArchivedAtErrorComponent |
            ApiV1PricingRulesUpdateArchivedErrorComponent | ApiV1PricingRulesUpdateArchivedReasonErrorComponent |
            ApiV1PricingRulesUpdateCriticalityErrorComponent | ApiV1PricingRulesUpdateDebugModeErrorComponent |
            ApiV1PricingRulesUpdateDiscountTypeErrorComponent | ApiV1PricingRulesUpdateDiscountValueErrorComponent |
            ApiV1PricingRulesUpdateDisplayNameErrorComponent | ApiV1PricingRulesUpdateKindErrorComponent |
            ApiV1PricingRulesUpdateLabelsErrorComponent | ApiV1PricingRulesUpdateNameErrorComponent |
            ApiV1PricingRulesUpdateNonFieldErrorsErrorComponent | ApiV1PricingRulesUpdatePlatformServiceErrorComponent |
            ApiV1PricingRulesUpdateProductKindErrorComponent | ApiV1PricingRulesUpdateProviderErrorComponent |
            ApiV1PricingRulesUpdateProviderIdErrorComponent | ApiV1PricingRulesUpdateProviderReferenceErrorComponent |
            ApiV1PricingRulesUpdateReconciliationEnabledErrorComponent |
            ApiV1PricingRulesUpdateSlaAvailabilityErrorComponent | ApiV1PricingRulesUpdateSlaTargetErrorComponent |
            ApiV1PricingRulesUpdateSloAvailabilityErrorComponent | ApiV1PricingRulesUpdateSloTargetErrorComponent |
            ApiV1PricingRulesUpdateTargetAvailabilityErrorComponent | ApiV1PricingRulesUpdateTolerationsErrorComponent]):
    """

    type_: ValidationErrorEnum
    errors: list[
        ApiV1PricingRulesUpdateActiveFromErrorComponent
        | ApiV1PricingRulesUpdateActiveUntilErrorComponent
        | ApiV1PricingRulesUpdateAnnotationsErrorComponent
        | ApiV1PricingRulesUpdateArchivedAtErrorComponent
        | ApiV1PricingRulesUpdateArchivedErrorComponent
        | ApiV1PricingRulesUpdateArchivedReasonErrorComponent
        | ApiV1PricingRulesUpdateCriticalityErrorComponent
        | ApiV1PricingRulesUpdateDebugModeErrorComponent
        | ApiV1PricingRulesUpdateDiscountTypeErrorComponent
        | ApiV1PricingRulesUpdateDiscountValueErrorComponent
        | ApiV1PricingRulesUpdateDisplayNameErrorComponent
        | ApiV1PricingRulesUpdateKindErrorComponent
        | ApiV1PricingRulesUpdateLabelsErrorComponent
        | ApiV1PricingRulesUpdateNameErrorComponent
        | ApiV1PricingRulesUpdateNonFieldErrorsErrorComponent
        | ApiV1PricingRulesUpdatePlatformServiceErrorComponent
        | ApiV1PricingRulesUpdateProductKindErrorComponent
        | ApiV1PricingRulesUpdateProviderErrorComponent
        | ApiV1PricingRulesUpdateProviderIdErrorComponent
        | ApiV1PricingRulesUpdateProviderReferenceErrorComponent
        | ApiV1PricingRulesUpdateReconciliationEnabledErrorComponent
        | ApiV1PricingRulesUpdateSlaAvailabilityErrorComponent
        | ApiV1PricingRulesUpdateSlaTargetErrorComponent
        | ApiV1PricingRulesUpdateSloAvailabilityErrorComponent
        | ApiV1PricingRulesUpdateSloTargetErrorComponent
        | ApiV1PricingRulesUpdateTargetAvailabilityErrorComponent
        | ApiV1PricingRulesUpdateTolerationsErrorComponent
    ]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.api_v1_pricing_rules_update_active_from_error_component import (
            ApiV1PricingRulesUpdateActiveFromErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_rules_update_annotations_error_component import (
            ApiV1PricingRulesUpdateAnnotationsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_rules_update_archived_at_error_component import (
            ApiV1PricingRulesUpdateArchivedAtErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_rules_update_archived_error_component import (
            ApiV1PricingRulesUpdateArchivedErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_rules_update_archived_reason_error_component import (
            ApiV1PricingRulesUpdateArchivedReasonErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_rules_update_criticality_error_component import (
            ApiV1PricingRulesUpdateCriticalityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_rules_update_debug_mode_error_component import (
            ApiV1PricingRulesUpdateDebugModeErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_rules_update_discount_type_error_component import (
            ApiV1PricingRulesUpdateDiscountTypeErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_rules_update_discount_value_error_component import (
            ApiV1PricingRulesUpdateDiscountValueErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_rules_update_display_name_error_component import (
            ApiV1PricingRulesUpdateDisplayNameErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_rules_update_kind_error_component import (
            ApiV1PricingRulesUpdateKindErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_rules_update_labels_error_component import (
            ApiV1PricingRulesUpdateLabelsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_rules_update_name_error_component import (
            ApiV1PricingRulesUpdateNameErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_rules_update_non_field_errors_error_component import (
            ApiV1PricingRulesUpdateNonFieldErrorsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_rules_update_platform_service_error_component import (
            ApiV1PricingRulesUpdatePlatformServiceErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_rules_update_product_kind_error_component import (
            ApiV1PricingRulesUpdateProductKindErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_rules_update_provider_error_component import (
            ApiV1PricingRulesUpdateProviderErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_rules_update_provider_id_error_component import (
            ApiV1PricingRulesUpdateProviderIdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_rules_update_provider_reference_error_component import (
            ApiV1PricingRulesUpdateProviderReferenceErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_rules_update_reconciliation_enabled_error_component import (
            ApiV1PricingRulesUpdateReconciliationEnabledErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_rules_update_sla_availability_error_component import (
            ApiV1PricingRulesUpdateSlaAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_rules_update_sla_target_error_component import (
            ApiV1PricingRulesUpdateSlaTargetErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_rules_update_slo_availability_error_component import (
            ApiV1PricingRulesUpdateSloAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_rules_update_slo_target_error_component import (
            ApiV1PricingRulesUpdateSloTargetErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_rules_update_target_availability_error_component import (
            ApiV1PricingRulesUpdateTargetAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_rules_update_tolerations_error_component import (
            ApiV1PricingRulesUpdateTolerationsErrorComponent,  # noqa: PLC0415
        )

        type_: str = self.type_

        errors = []
        for errors_item_data in self.errors:
            errors_item: dict[str, Any]
            if isinstance(errors_item_data, ApiV1PricingRulesUpdateNonFieldErrorsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingRulesUpdateNameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingRulesUpdateDisplayNameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingRulesUpdateLabelsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingRulesUpdateAnnotationsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingRulesUpdateDebugModeErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingRulesUpdateProviderErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingRulesUpdateProviderReferenceErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingRulesUpdateProviderIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingRulesUpdateReconciliationEnabledErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingRulesUpdatePlatformServiceErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingRulesUpdateKindErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingRulesUpdateTolerationsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingRulesUpdateArchivedErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingRulesUpdateArchivedAtErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingRulesUpdateArchivedReasonErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingRulesUpdateCriticalityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingRulesUpdateTargetAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingRulesUpdateSloTargetErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingRulesUpdateSloAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingRulesUpdateSlaTargetErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingRulesUpdateSlaAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingRulesUpdateProductKindErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingRulesUpdateDiscountTypeErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingRulesUpdateDiscountValueErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingRulesUpdateActiveFromErrorComponent):
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
        from ..models.api_v1_pricing_rules_update_active_from_error_component import (
            ApiV1PricingRulesUpdateActiveFromErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_rules_update_active_until_error_component import (
            ApiV1PricingRulesUpdateActiveUntilErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_rules_update_annotations_error_component import (
            ApiV1PricingRulesUpdateAnnotationsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_rules_update_archived_at_error_component import (
            ApiV1PricingRulesUpdateArchivedAtErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_rules_update_archived_error_component import (
            ApiV1PricingRulesUpdateArchivedErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_rules_update_archived_reason_error_component import (
            ApiV1PricingRulesUpdateArchivedReasonErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_rules_update_criticality_error_component import (
            ApiV1PricingRulesUpdateCriticalityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_rules_update_debug_mode_error_component import (
            ApiV1PricingRulesUpdateDebugModeErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_rules_update_discount_type_error_component import (
            ApiV1PricingRulesUpdateDiscountTypeErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_rules_update_discount_value_error_component import (
            ApiV1PricingRulesUpdateDiscountValueErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_rules_update_display_name_error_component import (
            ApiV1PricingRulesUpdateDisplayNameErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_rules_update_kind_error_component import (
            ApiV1PricingRulesUpdateKindErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_rules_update_labels_error_component import (
            ApiV1PricingRulesUpdateLabelsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_rules_update_name_error_component import (
            ApiV1PricingRulesUpdateNameErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_rules_update_non_field_errors_error_component import (
            ApiV1PricingRulesUpdateNonFieldErrorsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_rules_update_platform_service_error_component import (
            ApiV1PricingRulesUpdatePlatformServiceErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_rules_update_product_kind_error_component import (
            ApiV1PricingRulesUpdateProductKindErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_rules_update_provider_error_component import (
            ApiV1PricingRulesUpdateProviderErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_rules_update_provider_id_error_component import (
            ApiV1PricingRulesUpdateProviderIdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_rules_update_provider_reference_error_component import (
            ApiV1PricingRulesUpdateProviderReferenceErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_rules_update_reconciliation_enabled_error_component import (
            ApiV1PricingRulesUpdateReconciliationEnabledErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_rules_update_sla_availability_error_component import (
            ApiV1PricingRulesUpdateSlaAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_rules_update_sla_target_error_component import (
            ApiV1PricingRulesUpdateSlaTargetErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_rules_update_slo_availability_error_component import (
            ApiV1PricingRulesUpdateSloAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_rules_update_slo_target_error_component import (
            ApiV1PricingRulesUpdateSloTargetErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_rules_update_target_availability_error_component import (
            ApiV1PricingRulesUpdateTargetAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_rules_update_tolerations_error_component import (
            ApiV1PricingRulesUpdateTolerationsErrorComponent,  # noqa: PLC0415
        )

        d = dict(src_dict)
        type_ = check_validation_error_enum(d.pop("type"))

        errors = []
        _errors = d.pop("errors")
        for errors_item_data in _errors:

            def _parse_errors_item(
                data: object,
            ) -> (
                ApiV1PricingRulesUpdateActiveFromErrorComponent
                | ApiV1PricingRulesUpdateActiveUntilErrorComponent
                | ApiV1PricingRulesUpdateAnnotationsErrorComponent
                | ApiV1PricingRulesUpdateArchivedAtErrorComponent
                | ApiV1PricingRulesUpdateArchivedErrorComponent
                | ApiV1PricingRulesUpdateArchivedReasonErrorComponent
                | ApiV1PricingRulesUpdateCriticalityErrorComponent
                | ApiV1PricingRulesUpdateDebugModeErrorComponent
                | ApiV1PricingRulesUpdateDiscountTypeErrorComponent
                | ApiV1PricingRulesUpdateDiscountValueErrorComponent
                | ApiV1PricingRulesUpdateDisplayNameErrorComponent
                | ApiV1PricingRulesUpdateKindErrorComponent
                | ApiV1PricingRulesUpdateLabelsErrorComponent
                | ApiV1PricingRulesUpdateNameErrorComponent
                | ApiV1PricingRulesUpdateNonFieldErrorsErrorComponent
                | ApiV1PricingRulesUpdatePlatformServiceErrorComponent
                | ApiV1PricingRulesUpdateProductKindErrorComponent
                | ApiV1PricingRulesUpdateProviderErrorComponent
                | ApiV1PricingRulesUpdateProviderIdErrorComponent
                | ApiV1PricingRulesUpdateProviderReferenceErrorComponent
                | ApiV1PricingRulesUpdateReconciliationEnabledErrorComponent
                | ApiV1PricingRulesUpdateSlaAvailabilityErrorComponent
                | ApiV1PricingRulesUpdateSlaTargetErrorComponent
                | ApiV1PricingRulesUpdateSloAvailabilityErrorComponent
                | ApiV1PricingRulesUpdateSloTargetErrorComponent
                | ApiV1PricingRulesUpdateTargetAvailabilityErrorComponent
                | ApiV1PricingRulesUpdateTolerationsErrorComponent
            ):
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_rules_update_error_type_0 = (
                        ApiV1PricingRulesUpdateNonFieldErrorsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_rules_update_error_type_0
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_rules_update_error_type_1 = (
                        ApiV1PricingRulesUpdateNameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_rules_update_error_type_1
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_rules_update_error_type_2 = (
                        ApiV1PricingRulesUpdateDisplayNameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_rules_update_error_type_2
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_rules_update_error_type_3 = (
                        ApiV1PricingRulesUpdateLabelsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_rules_update_error_type_3
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_rules_update_error_type_4 = (
                        ApiV1PricingRulesUpdateAnnotationsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_rules_update_error_type_4
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_rules_update_error_type_5 = (
                        ApiV1PricingRulesUpdateDebugModeErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_rules_update_error_type_5
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_rules_update_error_type_6 = (
                        ApiV1PricingRulesUpdateProviderErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_rules_update_error_type_6
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_rules_update_error_type_7 = (
                        ApiV1PricingRulesUpdateProviderReferenceErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_rules_update_error_type_7
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_rules_update_error_type_8 = (
                        ApiV1PricingRulesUpdateProviderIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_rules_update_error_type_8
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_rules_update_error_type_9 = (
                        ApiV1PricingRulesUpdateReconciliationEnabledErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_rules_update_error_type_9
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_rules_update_error_type_10 = (
                        ApiV1PricingRulesUpdatePlatformServiceErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_rules_update_error_type_10
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_rules_update_error_type_11 = (
                        ApiV1PricingRulesUpdateKindErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_rules_update_error_type_11
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_rules_update_error_type_12 = (
                        ApiV1PricingRulesUpdateTolerationsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_rules_update_error_type_12
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_rules_update_error_type_13 = (
                        ApiV1PricingRulesUpdateArchivedErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_rules_update_error_type_13
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_rules_update_error_type_14 = (
                        ApiV1PricingRulesUpdateArchivedAtErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_rules_update_error_type_14
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_rules_update_error_type_15 = (
                        ApiV1PricingRulesUpdateArchivedReasonErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_rules_update_error_type_15
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_rules_update_error_type_16 = (
                        ApiV1PricingRulesUpdateCriticalityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_rules_update_error_type_16
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_rules_update_error_type_17 = (
                        ApiV1PricingRulesUpdateTargetAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_rules_update_error_type_17
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_rules_update_error_type_18 = (
                        ApiV1PricingRulesUpdateSloTargetErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_rules_update_error_type_18
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_rules_update_error_type_19 = (
                        ApiV1PricingRulesUpdateSloAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_rules_update_error_type_19
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_rules_update_error_type_20 = (
                        ApiV1PricingRulesUpdateSlaTargetErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_rules_update_error_type_20
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_rules_update_error_type_21 = (
                        ApiV1PricingRulesUpdateSlaAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_rules_update_error_type_21
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_rules_update_error_type_22 = (
                        ApiV1PricingRulesUpdateProductKindErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_rules_update_error_type_22
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_rules_update_error_type_23 = (
                        ApiV1PricingRulesUpdateDiscountTypeErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_rules_update_error_type_23
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_rules_update_error_type_24 = (
                        ApiV1PricingRulesUpdateDiscountValueErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_rules_update_error_type_24
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_rules_update_error_type_25 = (
                        ApiV1PricingRulesUpdateActiveFromErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_rules_update_error_type_25
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_api_v1_pricing_rules_update_error_type_26 = (
                    ApiV1PricingRulesUpdateActiveUntilErrorComponent.from_dict(data)
                )

                return componentsschemas_api_v1_pricing_rules_update_error_type_26

            errors_item = _parse_errors_item(errors_item_data)

            errors.append(errors_item)

        api_v1_pricing_rules_update_validation_error = cls(
            type_=type_,
            errors=errors,
        )

        api_v1_pricing_rules_update_validation_error.additional_properties = d
        return api_v1_pricing_rules_update_validation_error

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
