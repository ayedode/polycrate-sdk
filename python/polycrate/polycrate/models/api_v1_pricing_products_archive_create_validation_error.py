from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.validation_error_enum import ValidationErrorEnum, check_validation_error_enum

if TYPE_CHECKING:
    from ..models.api_v1_pricing_products_archive_create_annotations_error_component import (
        ApiV1PricingProductsArchiveCreateAnnotationsErrorComponent,
    )
    from ..models.api_v1_pricing_products_archive_create_archived_at_error_component import (
        ApiV1PricingProductsArchiveCreateArchivedAtErrorComponent,
    )
    from ..models.api_v1_pricing_products_archive_create_archived_error_component import (
        ApiV1PricingProductsArchiveCreateArchivedErrorComponent,
    )
    from ..models.api_v1_pricing_products_archive_create_archived_reason_error_component import (
        ApiV1PricingProductsArchiveCreateArchivedReasonErrorComponent,
    )
    from ..models.api_v1_pricing_products_archive_create_billing_interval_error_component import (
        ApiV1PricingProductsArchiveCreateBillingIntervalErrorComponent,
    )
    from ..models.api_v1_pricing_products_archive_create_config_error_component import (
        ApiV1PricingProductsArchiveCreateConfigErrorComponent,
    )
    from ..models.api_v1_pricing_products_archive_create_cost_per_unit_error_component import (
        ApiV1PricingProductsArchiveCreateCostPerUnitErrorComponent,
    )
    from ..models.api_v1_pricing_products_archive_create_criticality_error_component import (
        ApiV1PricingProductsArchiveCreateCriticalityErrorComponent,
    )
    from ..models.api_v1_pricing_products_archive_create_debug_mode_error_component import (
        ApiV1PricingProductsArchiveCreateDebugModeErrorComponent,
    )
    from ..models.api_v1_pricing_products_archive_create_display_name_error_component import (
        ApiV1PricingProductsArchiveCreateDisplayNameErrorComponent,
    )
    from ..models.api_v1_pricing_products_archive_create_kind_error_component import (
        ApiV1PricingProductsArchiveCreateKindErrorComponent,
    )
    from ..models.api_v1_pricing_products_archive_create_labels_error_component import (
        ApiV1PricingProductsArchiveCreateLabelsErrorComponent,
    )
    from ..models.api_v1_pricing_products_archive_create_name_error_component import (
        ApiV1PricingProductsArchiveCreateNameErrorComponent,
    )
    from ..models.api_v1_pricing_products_archive_create_non_field_errors_error_component import (
        ApiV1PricingProductsArchiveCreateNonFieldErrorsErrorComponent,
    )
    from ..models.api_v1_pricing_products_archive_create_platform_service_error_component import (
        ApiV1PricingProductsArchiveCreatePlatformServiceErrorComponent,
    )
    from ..models.api_v1_pricing_products_archive_create_price_per_unit_error_component import (
        ApiV1PricingProductsArchiveCreatePricePerUnitErrorComponent,
    )
    from ..models.api_v1_pricing_products_archive_create_provider_entity_error_component import (
        ApiV1PricingProductsArchiveCreateProviderEntityErrorComponent,
    )
    from ..models.api_v1_pricing_products_archive_create_provider_error_component import (
        ApiV1PricingProductsArchiveCreateProviderErrorComponent,
    )
    from ..models.api_v1_pricing_products_archive_create_provider_id_error_component import (
        ApiV1PricingProductsArchiveCreateProviderIdErrorComponent,
    )
    from ..models.api_v1_pricing_products_archive_create_provider_reference_error_component import (
        ApiV1PricingProductsArchiveCreateProviderReferenceErrorComponent,
    )
    from ..models.api_v1_pricing_products_archive_create_provider_type_id_error_component import (
        ApiV1PricingProductsArchiveCreateProviderTypeIdErrorComponent,
    )
    from ..models.api_v1_pricing_products_archive_create_reconciliation_enabled_error_component import (
        ApiV1PricingProductsArchiveCreateReconciliationEnabledErrorComponent,
    )
    from ..models.api_v1_pricing_products_archive_create_sla_availability_error_component import (
        ApiV1PricingProductsArchiveCreateSlaAvailabilityErrorComponent,
    )
    from ..models.api_v1_pricing_products_archive_create_sla_target_error_component import (
        ApiV1PricingProductsArchiveCreateSlaTargetErrorComponent,
    )
    from ..models.api_v1_pricing_products_archive_create_slo_availability_error_component import (
        ApiV1PricingProductsArchiveCreateSloAvailabilityErrorComponent,
    )
    from ..models.api_v1_pricing_products_archive_create_slo_target_error_component import (
        ApiV1PricingProductsArchiveCreateSloTargetErrorComponent,
    )
    from ..models.api_v1_pricing_products_archive_create_target_availability_error_component import (
        ApiV1PricingProductsArchiveCreateTargetAvailabilityErrorComponent,
    )
    from ..models.api_v1_pricing_products_archive_create_tolerations_error_component import (
        ApiV1PricingProductsArchiveCreateTolerationsErrorComponent,
    )


T = TypeVar("T", bound="ApiV1PricingProductsArchiveCreateValidationError")


@_attrs_define
class ApiV1PricingProductsArchiveCreateValidationError:
    """
    Attributes:
        type_ (ValidationErrorEnum): * `validation_error` - Validation Error
        errors (list[ApiV1PricingProductsArchiveCreateAnnotationsErrorComponent |
            ApiV1PricingProductsArchiveCreateArchivedAtErrorComponent |
            ApiV1PricingProductsArchiveCreateArchivedErrorComponent |
            ApiV1PricingProductsArchiveCreateArchivedReasonErrorComponent |
            ApiV1PricingProductsArchiveCreateBillingIntervalErrorComponent |
            ApiV1PricingProductsArchiveCreateConfigErrorComponent |
            ApiV1PricingProductsArchiveCreateCostPerUnitErrorComponent |
            ApiV1PricingProductsArchiveCreateCriticalityErrorComponent |
            ApiV1PricingProductsArchiveCreateDebugModeErrorComponent |
            ApiV1PricingProductsArchiveCreateDisplayNameErrorComponent | ApiV1PricingProductsArchiveCreateKindErrorComponent
            | ApiV1PricingProductsArchiveCreateLabelsErrorComponent | ApiV1PricingProductsArchiveCreateNameErrorComponent |
            ApiV1PricingProductsArchiveCreateNonFieldErrorsErrorComponent |
            ApiV1PricingProductsArchiveCreatePlatformServiceErrorComponent |
            ApiV1PricingProductsArchiveCreatePricePerUnitErrorComponent |
            ApiV1PricingProductsArchiveCreateProviderEntityErrorComponent |
            ApiV1PricingProductsArchiveCreateProviderErrorComponent |
            ApiV1PricingProductsArchiveCreateProviderIdErrorComponent |
            ApiV1PricingProductsArchiveCreateProviderReferenceErrorComponent |
            ApiV1PricingProductsArchiveCreateProviderTypeIdErrorComponent |
            ApiV1PricingProductsArchiveCreateReconciliationEnabledErrorComponent |
            ApiV1PricingProductsArchiveCreateSlaAvailabilityErrorComponent |
            ApiV1PricingProductsArchiveCreateSlaTargetErrorComponent |
            ApiV1PricingProductsArchiveCreateSloAvailabilityErrorComponent |
            ApiV1PricingProductsArchiveCreateSloTargetErrorComponent |
            ApiV1PricingProductsArchiveCreateTargetAvailabilityErrorComponent |
            ApiV1PricingProductsArchiveCreateTolerationsErrorComponent]):
    """

    type_: ValidationErrorEnum
    errors: list[
        ApiV1PricingProductsArchiveCreateAnnotationsErrorComponent
        | ApiV1PricingProductsArchiveCreateArchivedAtErrorComponent
        | ApiV1PricingProductsArchiveCreateArchivedErrorComponent
        | ApiV1PricingProductsArchiveCreateArchivedReasonErrorComponent
        | ApiV1PricingProductsArchiveCreateBillingIntervalErrorComponent
        | ApiV1PricingProductsArchiveCreateConfigErrorComponent
        | ApiV1PricingProductsArchiveCreateCostPerUnitErrorComponent
        | ApiV1PricingProductsArchiveCreateCriticalityErrorComponent
        | ApiV1PricingProductsArchiveCreateDebugModeErrorComponent
        | ApiV1PricingProductsArchiveCreateDisplayNameErrorComponent
        | ApiV1PricingProductsArchiveCreateKindErrorComponent
        | ApiV1PricingProductsArchiveCreateLabelsErrorComponent
        | ApiV1PricingProductsArchiveCreateNameErrorComponent
        | ApiV1PricingProductsArchiveCreateNonFieldErrorsErrorComponent
        | ApiV1PricingProductsArchiveCreatePlatformServiceErrorComponent
        | ApiV1PricingProductsArchiveCreatePricePerUnitErrorComponent
        | ApiV1PricingProductsArchiveCreateProviderEntityErrorComponent
        | ApiV1PricingProductsArchiveCreateProviderErrorComponent
        | ApiV1PricingProductsArchiveCreateProviderIdErrorComponent
        | ApiV1PricingProductsArchiveCreateProviderReferenceErrorComponent
        | ApiV1PricingProductsArchiveCreateProviderTypeIdErrorComponent
        | ApiV1PricingProductsArchiveCreateReconciliationEnabledErrorComponent
        | ApiV1PricingProductsArchiveCreateSlaAvailabilityErrorComponent
        | ApiV1PricingProductsArchiveCreateSlaTargetErrorComponent
        | ApiV1PricingProductsArchiveCreateSloAvailabilityErrorComponent
        | ApiV1PricingProductsArchiveCreateSloTargetErrorComponent
        | ApiV1PricingProductsArchiveCreateTargetAvailabilityErrorComponent
        | ApiV1PricingProductsArchiveCreateTolerationsErrorComponent
    ]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.api_v1_pricing_products_archive_create_annotations_error_component import (
            ApiV1PricingProductsArchiveCreateAnnotationsErrorComponent,
        )
        from ..models.api_v1_pricing_products_archive_create_archived_at_error_component import (
            ApiV1PricingProductsArchiveCreateArchivedAtErrorComponent,
        )
        from ..models.api_v1_pricing_products_archive_create_archived_error_component import (
            ApiV1PricingProductsArchiveCreateArchivedErrorComponent,
        )
        from ..models.api_v1_pricing_products_archive_create_archived_reason_error_component import (
            ApiV1PricingProductsArchiveCreateArchivedReasonErrorComponent,
        )
        from ..models.api_v1_pricing_products_archive_create_billing_interval_error_component import (
            ApiV1PricingProductsArchiveCreateBillingIntervalErrorComponent,
        )
        from ..models.api_v1_pricing_products_archive_create_cost_per_unit_error_component import (
            ApiV1PricingProductsArchiveCreateCostPerUnitErrorComponent,
        )
        from ..models.api_v1_pricing_products_archive_create_criticality_error_component import (
            ApiV1PricingProductsArchiveCreateCriticalityErrorComponent,
        )
        from ..models.api_v1_pricing_products_archive_create_debug_mode_error_component import (
            ApiV1PricingProductsArchiveCreateDebugModeErrorComponent,
        )
        from ..models.api_v1_pricing_products_archive_create_display_name_error_component import (
            ApiV1PricingProductsArchiveCreateDisplayNameErrorComponent,
        )
        from ..models.api_v1_pricing_products_archive_create_kind_error_component import (
            ApiV1PricingProductsArchiveCreateKindErrorComponent,
        )
        from ..models.api_v1_pricing_products_archive_create_labels_error_component import (
            ApiV1PricingProductsArchiveCreateLabelsErrorComponent,
        )
        from ..models.api_v1_pricing_products_archive_create_name_error_component import (
            ApiV1PricingProductsArchiveCreateNameErrorComponent,
        )
        from ..models.api_v1_pricing_products_archive_create_non_field_errors_error_component import (
            ApiV1PricingProductsArchiveCreateNonFieldErrorsErrorComponent,
        )
        from ..models.api_v1_pricing_products_archive_create_platform_service_error_component import (
            ApiV1PricingProductsArchiveCreatePlatformServiceErrorComponent,
        )
        from ..models.api_v1_pricing_products_archive_create_price_per_unit_error_component import (
            ApiV1PricingProductsArchiveCreatePricePerUnitErrorComponent,
        )
        from ..models.api_v1_pricing_products_archive_create_provider_entity_error_component import (
            ApiV1PricingProductsArchiveCreateProviderEntityErrorComponent,
        )
        from ..models.api_v1_pricing_products_archive_create_provider_error_component import (
            ApiV1PricingProductsArchiveCreateProviderErrorComponent,
        )
        from ..models.api_v1_pricing_products_archive_create_provider_id_error_component import (
            ApiV1PricingProductsArchiveCreateProviderIdErrorComponent,
        )
        from ..models.api_v1_pricing_products_archive_create_provider_reference_error_component import (
            ApiV1PricingProductsArchiveCreateProviderReferenceErrorComponent,
        )
        from ..models.api_v1_pricing_products_archive_create_provider_type_id_error_component import (
            ApiV1PricingProductsArchiveCreateProviderTypeIdErrorComponent,
        )
        from ..models.api_v1_pricing_products_archive_create_reconciliation_enabled_error_component import (
            ApiV1PricingProductsArchiveCreateReconciliationEnabledErrorComponent,
        )
        from ..models.api_v1_pricing_products_archive_create_sla_availability_error_component import (
            ApiV1PricingProductsArchiveCreateSlaAvailabilityErrorComponent,
        )
        from ..models.api_v1_pricing_products_archive_create_sla_target_error_component import (
            ApiV1PricingProductsArchiveCreateSlaTargetErrorComponent,
        )
        from ..models.api_v1_pricing_products_archive_create_slo_availability_error_component import (
            ApiV1PricingProductsArchiveCreateSloAvailabilityErrorComponent,
        )
        from ..models.api_v1_pricing_products_archive_create_slo_target_error_component import (
            ApiV1PricingProductsArchiveCreateSloTargetErrorComponent,
        )
        from ..models.api_v1_pricing_products_archive_create_target_availability_error_component import (
            ApiV1PricingProductsArchiveCreateTargetAvailabilityErrorComponent,
        )
        from ..models.api_v1_pricing_products_archive_create_tolerations_error_component import (
            ApiV1PricingProductsArchiveCreateTolerationsErrorComponent,
        )

        type_: str = self.type_

        errors = []
        for errors_item_data in self.errors:
            errors_item: dict[str, Any]
            if isinstance(errors_item_data, ApiV1PricingProductsArchiveCreateNonFieldErrorsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingProductsArchiveCreateNameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingProductsArchiveCreateDisplayNameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingProductsArchiveCreateLabelsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingProductsArchiveCreateAnnotationsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingProductsArchiveCreateDebugModeErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingProductsArchiveCreateProviderErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingProductsArchiveCreateProviderReferenceErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingProductsArchiveCreateProviderIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingProductsArchiveCreateReconciliationEnabledErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingProductsArchiveCreatePlatformServiceErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingProductsArchiveCreateKindErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingProductsArchiveCreateTolerationsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingProductsArchiveCreateArchivedErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingProductsArchiveCreateArchivedAtErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingProductsArchiveCreateArchivedReasonErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingProductsArchiveCreateCriticalityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingProductsArchiveCreateTargetAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingProductsArchiveCreateSloTargetErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingProductsArchiveCreateSloAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingProductsArchiveCreateSlaTargetErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingProductsArchiveCreateSlaAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingProductsArchiveCreateBillingIntervalErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingProductsArchiveCreatePricePerUnitErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingProductsArchiveCreateCostPerUnitErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingProductsArchiveCreateProviderEntityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingProductsArchiveCreateProviderTypeIdErrorComponent):
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
        from ..models.api_v1_pricing_products_archive_create_annotations_error_component import (
            ApiV1PricingProductsArchiveCreateAnnotationsErrorComponent,
        )
        from ..models.api_v1_pricing_products_archive_create_archived_at_error_component import (
            ApiV1PricingProductsArchiveCreateArchivedAtErrorComponent,
        )
        from ..models.api_v1_pricing_products_archive_create_archived_error_component import (
            ApiV1PricingProductsArchiveCreateArchivedErrorComponent,
        )
        from ..models.api_v1_pricing_products_archive_create_archived_reason_error_component import (
            ApiV1PricingProductsArchiveCreateArchivedReasonErrorComponent,
        )
        from ..models.api_v1_pricing_products_archive_create_billing_interval_error_component import (
            ApiV1PricingProductsArchiveCreateBillingIntervalErrorComponent,
        )
        from ..models.api_v1_pricing_products_archive_create_config_error_component import (
            ApiV1PricingProductsArchiveCreateConfigErrorComponent,
        )
        from ..models.api_v1_pricing_products_archive_create_cost_per_unit_error_component import (
            ApiV1PricingProductsArchiveCreateCostPerUnitErrorComponent,
        )
        from ..models.api_v1_pricing_products_archive_create_criticality_error_component import (
            ApiV1PricingProductsArchiveCreateCriticalityErrorComponent,
        )
        from ..models.api_v1_pricing_products_archive_create_debug_mode_error_component import (
            ApiV1PricingProductsArchiveCreateDebugModeErrorComponent,
        )
        from ..models.api_v1_pricing_products_archive_create_display_name_error_component import (
            ApiV1PricingProductsArchiveCreateDisplayNameErrorComponent,
        )
        from ..models.api_v1_pricing_products_archive_create_kind_error_component import (
            ApiV1PricingProductsArchiveCreateKindErrorComponent,
        )
        from ..models.api_v1_pricing_products_archive_create_labels_error_component import (
            ApiV1PricingProductsArchiveCreateLabelsErrorComponent,
        )
        from ..models.api_v1_pricing_products_archive_create_name_error_component import (
            ApiV1PricingProductsArchiveCreateNameErrorComponent,
        )
        from ..models.api_v1_pricing_products_archive_create_non_field_errors_error_component import (
            ApiV1PricingProductsArchiveCreateNonFieldErrorsErrorComponent,
        )
        from ..models.api_v1_pricing_products_archive_create_platform_service_error_component import (
            ApiV1PricingProductsArchiveCreatePlatformServiceErrorComponent,
        )
        from ..models.api_v1_pricing_products_archive_create_price_per_unit_error_component import (
            ApiV1PricingProductsArchiveCreatePricePerUnitErrorComponent,
        )
        from ..models.api_v1_pricing_products_archive_create_provider_entity_error_component import (
            ApiV1PricingProductsArchiveCreateProviderEntityErrorComponent,
        )
        from ..models.api_v1_pricing_products_archive_create_provider_error_component import (
            ApiV1PricingProductsArchiveCreateProviderErrorComponent,
        )
        from ..models.api_v1_pricing_products_archive_create_provider_id_error_component import (
            ApiV1PricingProductsArchiveCreateProviderIdErrorComponent,
        )
        from ..models.api_v1_pricing_products_archive_create_provider_reference_error_component import (
            ApiV1PricingProductsArchiveCreateProviderReferenceErrorComponent,
        )
        from ..models.api_v1_pricing_products_archive_create_provider_type_id_error_component import (
            ApiV1PricingProductsArchiveCreateProviderTypeIdErrorComponent,
        )
        from ..models.api_v1_pricing_products_archive_create_reconciliation_enabled_error_component import (
            ApiV1PricingProductsArchiveCreateReconciliationEnabledErrorComponent,
        )
        from ..models.api_v1_pricing_products_archive_create_sla_availability_error_component import (
            ApiV1PricingProductsArchiveCreateSlaAvailabilityErrorComponent,
        )
        from ..models.api_v1_pricing_products_archive_create_sla_target_error_component import (
            ApiV1PricingProductsArchiveCreateSlaTargetErrorComponent,
        )
        from ..models.api_v1_pricing_products_archive_create_slo_availability_error_component import (
            ApiV1PricingProductsArchiveCreateSloAvailabilityErrorComponent,
        )
        from ..models.api_v1_pricing_products_archive_create_slo_target_error_component import (
            ApiV1PricingProductsArchiveCreateSloTargetErrorComponent,
        )
        from ..models.api_v1_pricing_products_archive_create_target_availability_error_component import (
            ApiV1PricingProductsArchiveCreateTargetAvailabilityErrorComponent,
        )
        from ..models.api_v1_pricing_products_archive_create_tolerations_error_component import (
            ApiV1PricingProductsArchiveCreateTolerationsErrorComponent,
        )

        d = dict(src_dict)
        type_ = check_validation_error_enum(d.pop("type"))

        errors = []
        _errors = d.pop("errors")
        for errors_item_data in _errors:

            def _parse_errors_item(
                data: object,
            ) -> (
                ApiV1PricingProductsArchiveCreateAnnotationsErrorComponent
                | ApiV1PricingProductsArchiveCreateArchivedAtErrorComponent
                | ApiV1PricingProductsArchiveCreateArchivedErrorComponent
                | ApiV1PricingProductsArchiveCreateArchivedReasonErrorComponent
                | ApiV1PricingProductsArchiveCreateBillingIntervalErrorComponent
                | ApiV1PricingProductsArchiveCreateConfigErrorComponent
                | ApiV1PricingProductsArchiveCreateCostPerUnitErrorComponent
                | ApiV1PricingProductsArchiveCreateCriticalityErrorComponent
                | ApiV1PricingProductsArchiveCreateDebugModeErrorComponent
                | ApiV1PricingProductsArchiveCreateDisplayNameErrorComponent
                | ApiV1PricingProductsArchiveCreateKindErrorComponent
                | ApiV1PricingProductsArchiveCreateLabelsErrorComponent
                | ApiV1PricingProductsArchiveCreateNameErrorComponent
                | ApiV1PricingProductsArchiveCreateNonFieldErrorsErrorComponent
                | ApiV1PricingProductsArchiveCreatePlatformServiceErrorComponent
                | ApiV1PricingProductsArchiveCreatePricePerUnitErrorComponent
                | ApiV1PricingProductsArchiveCreateProviderEntityErrorComponent
                | ApiV1PricingProductsArchiveCreateProviderErrorComponent
                | ApiV1PricingProductsArchiveCreateProviderIdErrorComponent
                | ApiV1PricingProductsArchiveCreateProviderReferenceErrorComponent
                | ApiV1PricingProductsArchiveCreateProviderTypeIdErrorComponent
                | ApiV1PricingProductsArchiveCreateReconciliationEnabledErrorComponent
                | ApiV1PricingProductsArchiveCreateSlaAvailabilityErrorComponent
                | ApiV1PricingProductsArchiveCreateSlaTargetErrorComponent
                | ApiV1PricingProductsArchiveCreateSloAvailabilityErrorComponent
                | ApiV1PricingProductsArchiveCreateSloTargetErrorComponent
                | ApiV1PricingProductsArchiveCreateTargetAvailabilityErrorComponent
                | ApiV1PricingProductsArchiveCreateTolerationsErrorComponent
            ):
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_products_archive_create_error_type_0 = (
                        ApiV1PricingProductsArchiveCreateNonFieldErrorsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_products_archive_create_error_type_0
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_products_archive_create_error_type_1 = (
                        ApiV1PricingProductsArchiveCreateNameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_products_archive_create_error_type_1
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_products_archive_create_error_type_2 = (
                        ApiV1PricingProductsArchiveCreateDisplayNameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_products_archive_create_error_type_2
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_products_archive_create_error_type_3 = (
                        ApiV1PricingProductsArchiveCreateLabelsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_products_archive_create_error_type_3
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_products_archive_create_error_type_4 = (
                        ApiV1PricingProductsArchiveCreateAnnotationsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_products_archive_create_error_type_4
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_products_archive_create_error_type_5 = (
                        ApiV1PricingProductsArchiveCreateDebugModeErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_products_archive_create_error_type_5
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_products_archive_create_error_type_6 = (
                        ApiV1PricingProductsArchiveCreateProviderErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_products_archive_create_error_type_6
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_products_archive_create_error_type_7 = (
                        ApiV1PricingProductsArchiveCreateProviderReferenceErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_products_archive_create_error_type_7
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_products_archive_create_error_type_8 = (
                        ApiV1PricingProductsArchiveCreateProviderIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_products_archive_create_error_type_8
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_products_archive_create_error_type_9 = (
                        ApiV1PricingProductsArchiveCreateReconciliationEnabledErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_products_archive_create_error_type_9
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_products_archive_create_error_type_10 = (
                        ApiV1PricingProductsArchiveCreatePlatformServiceErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_products_archive_create_error_type_10
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_products_archive_create_error_type_11 = (
                        ApiV1PricingProductsArchiveCreateKindErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_products_archive_create_error_type_11
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_products_archive_create_error_type_12 = (
                        ApiV1PricingProductsArchiveCreateTolerationsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_products_archive_create_error_type_12
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_products_archive_create_error_type_13 = (
                        ApiV1PricingProductsArchiveCreateArchivedErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_products_archive_create_error_type_13
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_products_archive_create_error_type_14 = (
                        ApiV1PricingProductsArchiveCreateArchivedAtErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_products_archive_create_error_type_14
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_products_archive_create_error_type_15 = (
                        ApiV1PricingProductsArchiveCreateArchivedReasonErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_products_archive_create_error_type_15
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_products_archive_create_error_type_16 = (
                        ApiV1PricingProductsArchiveCreateCriticalityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_products_archive_create_error_type_16
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_products_archive_create_error_type_17 = (
                        ApiV1PricingProductsArchiveCreateTargetAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_products_archive_create_error_type_17
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_products_archive_create_error_type_18 = (
                        ApiV1PricingProductsArchiveCreateSloTargetErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_products_archive_create_error_type_18
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_products_archive_create_error_type_19 = (
                        ApiV1PricingProductsArchiveCreateSloAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_products_archive_create_error_type_19
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_products_archive_create_error_type_20 = (
                        ApiV1PricingProductsArchiveCreateSlaTargetErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_products_archive_create_error_type_20
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_products_archive_create_error_type_21 = (
                        ApiV1PricingProductsArchiveCreateSlaAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_products_archive_create_error_type_21
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_products_archive_create_error_type_22 = (
                        ApiV1PricingProductsArchiveCreateBillingIntervalErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_products_archive_create_error_type_22
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_products_archive_create_error_type_23 = (
                        ApiV1PricingProductsArchiveCreatePricePerUnitErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_products_archive_create_error_type_23
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_products_archive_create_error_type_24 = (
                        ApiV1PricingProductsArchiveCreateCostPerUnitErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_products_archive_create_error_type_24
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_products_archive_create_error_type_25 = (
                        ApiV1PricingProductsArchiveCreateProviderEntityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_products_archive_create_error_type_25
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_products_archive_create_error_type_26 = (
                        ApiV1PricingProductsArchiveCreateProviderTypeIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_products_archive_create_error_type_26
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_api_v1_pricing_products_archive_create_error_type_27 = (
                    ApiV1PricingProductsArchiveCreateConfigErrorComponent.from_dict(data)
                )

                return componentsschemas_api_v1_pricing_products_archive_create_error_type_27

            errors_item = _parse_errors_item(errors_item_data)

            errors.append(errors_item)

        api_v1_pricing_products_archive_create_validation_error = cls(
            type_=type_,
            errors=errors,
        )

        api_v1_pricing_products_archive_create_validation_error.additional_properties = d
        return api_v1_pricing_products_archive_create_validation_error

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
