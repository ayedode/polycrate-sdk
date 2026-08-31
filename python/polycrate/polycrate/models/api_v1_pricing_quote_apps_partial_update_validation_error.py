from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.validation_error_enum import ValidationErrorEnum, check_validation_error_enum

if TYPE_CHECKING:
    from ..models.api_v1_pricing_quote_apps_partial_update_annotations_error_component import (
        ApiV1PricingQuoteAppsPartialUpdateAnnotationsErrorComponent,
    )
    from ..models.api_v1_pricing_quote_apps_partial_update_archived_at_error_component import (
        ApiV1PricingQuoteAppsPartialUpdateArchivedAtErrorComponent,
    )
    from ..models.api_v1_pricing_quote_apps_partial_update_archived_error_component import (
        ApiV1PricingQuoteAppsPartialUpdateArchivedErrorComponent,
    )
    from ..models.api_v1_pricing_quote_apps_partial_update_archived_reason_error_component import (
        ApiV1PricingQuoteAppsPartialUpdateArchivedReasonErrorComponent,
    )
    from ..models.api_v1_pricing_quote_apps_partial_update_catalogue_app_error_component import (
        ApiV1PricingQuoteAppsPartialUpdateCatalogueAppErrorComponent,
    )
    from ..models.api_v1_pricing_quote_apps_partial_update_count_error_component import (
        ApiV1PricingQuoteAppsPartialUpdateCountErrorComponent,
    )
    from ..models.api_v1_pricing_quote_apps_partial_update_criticality_error_component import (
        ApiV1PricingQuoteAppsPartialUpdateCriticalityErrorComponent,
    )
    from ..models.api_v1_pricing_quote_apps_partial_update_debug_mode_error_component import (
        ApiV1PricingQuoteAppsPartialUpdateDebugModeErrorComponent,
    )
    from ..models.api_v1_pricing_quote_apps_partial_update_display_name_error_component import (
        ApiV1PricingQuoteAppsPartialUpdateDisplayNameErrorComponent,
    )
    from ..models.api_v1_pricing_quote_apps_partial_update_kind_error_component import (
        ApiV1PricingQuoteAppsPartialUpdateKindErrorComponent,
    )
    from ..models.api_v1_pricing_quote_apps_partial_update_labels_error_component import (
        ApiV1PricingQuoteAppsPartialUpdateLabelsErrorComponent,
    )
    from ..models.api_v1_pricing_quote_apps_partial_update_name_error_component import (
        ApiV1PricingQuoteAppsPartialUpdateNameErrorComponent,
    )
    from ..models.api_v1_pricing_quote_apps_partial_update_non_field_errors_error_component import (
        ApiV1PricingQuoteAppsPartialUpdateNonFieldErrorsErrorComponent,
    )
    from ..models.api_v1_pricing_quote_apps_partial_update_platform_service_error_component import (
        ApiV1PricingQuoteAppsPartialUpdatePlatformServiceErrorComponent,
    )
    from ..models.api_v1_pricing_quote_apps_partial_update_provider_error_component import (
        ApiV1PricingQuoteAppsPartialUpdateProviderErrorComponent,
    )
    from ..models.api_v1_pricing_quote_apps_partial_update_provider_id_error_component import (
        ApiV1PricingQuoteAppsPartialUpdateProviderIdErrorComponent,
    )
    from ..models.api_v1_pricing_quote_apps_partial_update_provider_reference_error_component import (
        ApiV1PricingQuoteAppsPartialUpdateProviderReferenceErrorComponent,
    )
    from ..models.api_v1_pricing_quote_apps_partial_update_quote_workspace_error_component import (
        ApiV1PricingQuoteAppsPartialUpdateQuoteWorkspaceErrorComponent,
    )
    from ..models.api_v1_pricing_quote_apps_partial_update_quoted_price_error_component import (
        ApiV1PricingQuoteAppsPartialUpdateQuotedPriceErrorComponent,
    )
    from ..models.api_v1_pricing_quote_apps_partial_update_reconciliation_enabled_error_component import (
        ApiV1PricingQuoteAppsPartialUpdateReconciliationEnabledErrorComponent,
    )
    from ..models.api_v1_pricing_quote_apps_partial_update_sla_availability_error_component import (
        ApiV1PricingQuoteAppsPartialUpdateSlaAvailabilityErrorComponent,
    )
    from ..models.api_v1_pricing_quote_apps_partial_update_sla_target_error_component import (
        ApiV1PricingQuoteAppsPartialUpdateSlaTargetErrorComponent,
    )
    from ..models.api_v1_pricing_quote_apps_partial_update_slo_availability_error_component import (
        ApiV1PricingQuoteAppsPartialUpdateSloAvailabilityErrorComponent,
    )
    from ..models.api_v1_pricing_quote_apps_partial_update_slo_target_error_component import (
        ApiV1PricingQuoteAppsPartialUpdateSloTargetErrorComponent,
    )
    from ..models.api_v1_pricing_quote_apps_partial_update_target_availability_error_component import (
        ApiV1PricingQuoteAppsPartialUpdateTargetAvailabilityErrorComponent,
    )
    from ..models.api_v1_pricing_quote_apps_partial_update_tolerations_error_component import (
        ApiV1PricingQuoteAppsPartialUpdateTolerationsErrorComponent,
    )


T = TypeVar("T", bound="ApiV1PricingQuoteAppsPartialUpdateValidationError")


@_attrs_define
class ApiV1PricingQuoteAppsPartialUpdateValidationError:
    """
    Attributes:
        type_ (ValidationErrorEnum): * `validation_error` - Validation Error
        errors (list[ApiV1PricingQuoteAppsPartialUpdateAnnotationsErrorComponent |
            ApiV1PricingQuoteAppsPartialUpdateArchivedAtErrorComponent |
            ApiV1PricingQuoteAppsPartialUpdateArchivedErrorComponent |
            ApiV1PricingQuoteAppsPartialUpdateArchivedReasonErrorComponent |
            ApiV1PricingQuoteAppsPartialUpdateCatalogueAppErrorComponent |
            ApiV1PricingQuoteAppsPartialUpdateCountErrorComponent |
            ApiV1PricingQuoteAppsPartialUpdateCriticalityErrorComponent |
            ApiV1PricingQuoteAppsPartialUpdateDebugModeErrorComponent |
            ApiV1PricingQuoteAppsPartialUpdateDisplayNameErrorComponent |
            ApiV1PricingQuoteAppsPartialUpdateKindErrorComponent | ApiV1PricingQuoteAppsPartialUpdateLabelsErrorComponent |
            ApiV1PricingQuoteAppsPartialUpdateNameErrorComponent |
            ApiV1PricingQuoteAppsPartialUpdateNonFieldErrorsErrorComponent |
            ApiV1PricingQuoteAppsPartialUpdatePlatformServiceErrorComponent |
            ApiV1PricingQuoteAppsPartialUpdateProviderErrorComponent |
            ApiV1PricingQuoteAppsPartialUpdateProviderIdErrorComponent |
            ApiV1PricingQuoteAppsPartialUpdateProviderReferenceErrorComponent |
            ApiV1PricingQuoteAppsPartialUpdateQuotedPriceErrorComponent |
            ApiV1PricingQuoteAppsPartialUpdateQuoteWorkspaceErrorComponent |
            ApiV1PricingQuoteAppsPartialUpdateReconciliationEnabledErrorComponent |
            ApiV1PricingQuoteAppsPartialUpdateSlaAvailabilityErrorComponent |
            ApiV1PricingQuoteAppsPartialUpdateSlaTargetErrorComponent |
            ApiV1PricingQuoteAppsPartialUpdateSloAvailabilityErrorComponent |
            ApiV1PricingQuoteAppsPartialUpdateSloTargetErrorComponent |
            ApiV1PricingQuoteAppsPartialUpdateTargetAvailabilityErrorComponent |
            ApiV1PricingQuoteAppsPartialUpdateTolerationsErrorComponent]):
    """

    type_: ValidationErrorEnum
    errors: list[
        ApiV1PricingQuoteAppsPartialUpdateAnnotationsErrorComponent
        | ApiV1PricingQuoteAppsPartialUpdateArchivedAtErrorComponent
        | ApiV1PricingQuoteAppsPartialUpdateArchivedErrorComponent
        | ApiV1PricingQuoteAppsPartialUpdateArchivedReasonErrorComponent
        | ApiV1PricingQuoteAppsPartialUpdateCatalogueAppErrorComponent
        | ApiV1PricingQuoteAppsPartialUpdateCountErrorComponent
        | ApiV1PricingQuoteAppsPartialUpdateCriticalityErrorComponent
        | ApiV1PricingQuoteAppsPartialUpdateDebugModeErrorComponent
        | ApiV1PricingQuoteAppsPartialUpdateDisplayNameErrorComponent
        | ApiV1PricingQuoteAppsPartialUpdateKindErrorComponent
        | ApiV1PricingQuoteAppsPartialUpdateLabelsErrorComponent
        | ApiV1PricingQuoteAppsPartialUpdateNameErrorComponent
        | ApiV1PricingQuoteAppsPartialUpdateNonFieldErrorsErrorComponent
        | ApiV1PricingQuoteAppsPartialUpdatePlatformServiceErrorComponent
        | ApiV1PricingQuoteAppsPartialUpdateProviderErrorComponent
        | ApiV1PricingQuoteAppsPartialUpdateProviderIdErrorComponent
        | ApiV1PricingQuoteAppsPartialUpdateProviderReferenceErrorComponent
        | ApiV1PricingQuoteAppsPartialUpdateQuotedPriceErrorComponent
        | ApiV1PricingQuoteAppsPartialUpdateQuoteWorkspaceErrorComponent
        | ApiV1PricingQuoteAppsPartialUpdateReconciliationEnabledErrorComponent
        | ApiV1PricingQuoteAppsPartialUpdateSlaAvailabilityErrorComponent
        | ApiV1PricingQuoteAppsPartialUpdateSlaTargetErrorComponent
        | ApiV1PricingQuoteAppsPartialUpdateSloAvailabilityErrorComponent
        | ApiV1PricingQuoteAppsPartialUpdateSloTargetErrorComponent
        | ApiV1PricingQuoteAppsPartialUpdateTargetAvailabilityErrorComponent
        | ApiV1PricingQuoteAppsPartialUpdateTolerationsErrorComponent
    ]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.api_v1_pricing_quote_apps_partial_update_annotations_error_component import (
            ApiV1PricingQuoteAppsPartialUpdateAnnotationsErrorComponent,
        )
        from ..models.api_v1_pricing_quote_apps_partial_update_archived_at_error_component import (
            ApiV1PricingQuoteAppsPartialUpdateArchivedAtErrorComponent,
        )
        from ..models.api_v1_pricing_quote_apps_partial_update_archived_error_component import (
            ApiV1PricingQuoteAppsPartialUpdateArchivedErrorComponent,
        )
        from ..models.api_v1_pricing_quote_apps_partial_update_archived_reason_error_component import (
            ApiV1PricingQuoteAppsPartialUpdateArchivedReasonErrorComponent,
        )
        from ..models.api_v1_pricing_quote_apps_partial_update_catalogue_app_error_component import (
            ApiV1PricingQuoteAppsPartialUpdateCatalogueAppErrorComponent,
        )
        from ..models.api_v1_pricing_quote_apps_partial_update_count_error_component import (
            ApiV1PricingQuoteAppsPartialUpdateCountErrorComponent,
        )
        from ..models.api_v1_pricing_quote_apps_partial_update_criticality_error_component import (
            ApiV1PricingQuoteAppsPartialUpdateCriticalityErrorComponent,
        )
        from ..models.api_v1_pricing_quote_apps_partial_update_debug_mode_error_component import (
            ApiV1PricingQuoteAppsPartialUpdateDebugModeErrorComponent,
        )
        from ..models.api_v1_pricing_quote_apps_partial_update_display_name_error_component import (
            ApiV1PricingQuoteAppsPartialUpdateDisplayNameErrorComponent,
        )
        from ..models.api_v1_pricing_quote_apps_partial_update_kind_error_component import (
            ApiV1PricingQuoteAppsPartialUpdateKindErrorComponent,
        )
        from ..models.api_v1_pricing_quote_apps_partial_update_labels_error_component import (
            ApiV1PricingQuoteAppsPartialUpdateLabelsErrorComponent,
        )
        from ..models.api_v1_pricing_quote_apps_partial_update_name_error_component import (
            ApiV1PricingQuoteAppsPartialUpdateNameErrorComponent,
        )
        from ..models.api_v1_pricing_quote_apps_partial_update_non_field_errors_error_component import (
            ApiV1PricingQuoteAppsPartialUpdateNonFieldErrorsErrorComponent,
        )
        from ..models.api_v1_pricing_quote_apps_partial_update_platform_service_error_component import (
            ApiV1PricingQuoteAppsPartialUpdatePlatformServiceErrorComponent,
        )
        from ..models.api_v1_pricing_quote_apps_partial_update_provider_error_component import (
            ApiV1PricingQuoteAppsPartialUpdateProviderErrorComponent,
        )
        from ..models.api_v1_pricing_quote_apps_partial_update_provider_id_error_component import (
            ApiV1PricingQuoteAppsPartialUpdateProviderIdErrorComponent,
        )
        from ..models.api_v1_pricing_quote_apps_partial_update_provider_reference_error_component import (
            ApiV1PricingQuoteAppsPartialUpdateProviderReferenceErrorComponent,
        )
        from ..models.api_v1_pricing_quote_apps_partial_update_quote_workspace_error_component import (
            ApiV1PricingQuoteAppsPartialUpdateQuoteWorkspaceErrorComponent,
        )
        from ..models.api_v1_pricing_quote_apps_partial_update_reconciliation_enabled_error_component import (
            ApiV1PricingQuoteAppsPartialUpdateReconciliationEnabledErrorComponent,
        )
        from ..models.api_v1_pricing_quote_apps_partial_update_sla_availability_error_component import (
            ApiV1PricingQuoteAppsPartialUpdateSlaAvailabilityErrorComponent,
        )
        from ..models.api_v1_pricing_quote_apps_partial_update_sla_target_error_component import (
            ApiV1PricingQuoteAppsPartialUpdateSlaTargetErrorComponent,
        )
        from ..models.api_v1_pricing_quote_apps_partial_update_slo_availability_error_component import (
            ApiV1PricingQuoteAppsPartialUpdateSloAvailabilityErrorComponent,
        )
        from ..models.api_v1_pricing_quote_apps_partial_update_slo_target_error_component import (
            ApiV1PricingQuoteAppsPartialUpdateSloTargetErrorComponent,
        )
        from ..models.api_v1_pricing_quote_apps_partial_update_target_availability_error_component import (
            ApiV1PricingQuoteAppsPartialUpdateTargetAvailabilityErrorComponent,
        )
        from ..models.api_v1_pricing_quote_apps_partial_update_tolerations_error_component import (
            ApiV1PricingQuoteAppsPartialUpdateTolerationsErrorComponent,
        )

        type_: str = self.type_

        errors = []
        for errors_item_data in self.errors:
            errors_item: dict[str, Any]
            if isinstance(errors_item_data, ApiV1PricingQuoteAppsPartialUpdateNonFieldErrorsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingQuoteAppsPartialUpdateNameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingQuoteAppsPartialUpdateDisplayNameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingQuoteAppsPartialUpdateLabelsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingQuoteAppsPartialUpdateAnnotationsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingQuoteAppsPartialUpdateDebugModeErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingQuoteAppsPartialUpdateProviderErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingQuoteAppsPartialUpdateProviderReferenceErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingQuoteAppsPartialUpdateProviderIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingQuoteAppsPartialUpdateReconciliationEnabledErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingQuoteAppsPartialUpdatePlatformServiceErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingQuoteAppsPartialUpdateKindErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingQuoteAppsPartialUpdateTolerationsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingQuoteAppsPartialUpdateArchivedErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingQuoteAppsPartialUpdateArchivedAtErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingQuoteAppsPartialUpdateArchivedReasonErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingQuoteAppsPartialUpdateCriticalityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingQuoteAppsPartialUpdateTargetAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingQuoteAppsPartialUpdateSloTargetErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingQuoteAppsPartialUpdateSloAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingQuoteAppsPartialUpdateSlaTargetErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingQuoteAppsPartialUpdateSlaAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingQuoteAppsPartialUpdateQuoteWorkspaceErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingQuoteAppsPartialUpdateCatalogueAppErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingQuoteAppsPartialUpdateCountErrorComponent):
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
        from ..models.api_v1_pricing_quote_apps_partial_update_annotations_error_component import (
            ApiV1PricingQuoteAppsPartialUpdateAnnotationsErrorComponent,
        )
        from ..models.api_v1_pricing_quote_apps_partial_update_archived_at_error_component import (
            ApiV1PricingQuoteAppsPartialUpdateArchivedAtErrorComponent,
        )
        from ..models.api_v1_pricing_quote_apps_partial_update_archived_error_component import (
            ApiV1PricingQuoteAppsPartialUpdateArchivedErrorComponent,
        )
        from ..models.api_v1_pricing_quote_apps_partial_update_archived_reason_error_component import (
            ApiV1PricingQuoteAppsPartialUpdateArchivedReasonErrorComponent,
        )
        from ..models.api_v1_pricing_quote_apps_partial_update_catalogue_app_error_component import (
            ApiV1PricingQuoteAppsPartialUpdateCatalogueAppErrorComponent,
        )
        from ..models.api_v1_pricing_quote_apps_partial_update_count_error_component import (
            ApiV1PricingQuoteAppsPartialUpdateCountErrorComponent,
        )
        from ..models.api_v1_pricing_quote_apps_partial_update_criticality_error_component import (
            ApiV1PricingQuoteAppsPartialUpdateCriticalityErrorComponent,
        )
        from ..models.api_v1_pricing_quote_apps_partial_update_debug_mode_error_component import (
            ApiV1PricingQuoteAppsPartialUpdateDebugModeErrorComponent,
        )
        from ..models.api_v1_pricing_quote_apps_partial_update_display_name_error_component import (
            ApiV1PricingQuoteAppsPartialUpdateDisplayNameErrorComponent,
        )
        from ..models.api_v1_pricing_quote_apps_partial_update_kind_error_component import (
            ApiV1PricingQuoteAppsPartialUpdateKindErrorComponent,
        )
        from ..models.api_v1_pricing_quote_apps_partial_update_labels_error_component import (
            ApiV1PricingQuoteAppsPartialUpdateLabelsErrorComponent,
        )
        from ..models.api_v1_pricing_quote_apps_partial_update_name_error_component import (
            ApiV1PricingQuoteAppsPartialUpdateNameErrorComponent,
        )
        from ..models.api_v1_pricing_quote_apps_partial_update_non_field_errors_error_component import (
            ApiV1PricingQuoteAppsPartialUpdateNonFieldErrorsErrorComponent,
        )
        from ..models.api_v1_pricing_quote_apps_partial_update_platform_service_error_component import (
            ApiV1PricingQuoteAppsPartialUpdatePlatformServiceErrorComponent,
        )
        from ..models.api_v1_pricing_quote_apps_partial_update_provider_error_component import (
            ApiV1PricingQuoteAppsPartialUpdateProviderErrorComponent,
        )
        from ..models.api_v1_pricing_quote_apps_partial_update_provider_id_error_component import (
            ApiV1PricingQuoteAppsPartialUpdateProviderIdErrorComponent,
        )
        from ..models.api_v1_pricing_quote_apps_partial_update_provider_reference_error_component import (
            ApiV1PricingQuoteAppsPartialUpdateProviderReferenceErrorComponent,
        )
        from ..models.api_v1_pricing_quote_apps_partial_update_quote_workspace_error_component import (
            ApiV1PricingQuoteAppsPartialUpdateQuoteWorkspaceErrorComponent,
        )
        from ..models.api_v1_pricing_quote_apps_partial_update_quoted_price_error_component import (
            ApiV1PricingQuoteAppsPartialUpdateQuotedPriceErrorComponent,
        )
        from ..models.api_v1_pricing_quote_apps_partial_update_reconciliation_enabled_error_component import (
            ApiV1PricingQuoteAppsPartialUpdateReconciliationEnabledErrorComponent,
        )
        from ..models.api_v1_pricing_quote_apps_partial_update_sla_availability_error_component import (
            ApiV1PricingQuoteAppsPartialUpdateSlaAvailabilityErrorComponent,
        )
        from ..models.api_v1_pricing_quote_apps_partial_update_sla_target_error_component import (
            ApiV1PricingQuoteAppsPartialUpdateSlaTargetErrorComponent,
        )
        from ..models.api_v1_pricing_quote_apps_partial_update_slo_availability_error_component import (
            ApiV1PricingQuoteAppsPartialUpdateSloAvailabilityErrorComponent,
        )
        from ..models.api_v1_pricing_quote_apps_partial_update_slo_target_error_component import (
            ApiV1PricingQuoteAppsPartialUpdateSloTargetErrorComponent,
        )
        from ..models.api_v1_pricing_quote_apps_partial_update_target_availability_error_component import (
            ApiV1PricingQuoteAppsPartialUpdateTargetAvailabilityErrorComponent,
        )
        from ..models.api_v1_pricing_quote_apps_partial_update_tolerations_error_component import (
            ApiV1PricingQuoteAppsPartialUpdateTolerationsErrorComponent,
        )

        d = dict(src_dict)
        type_ = check_validation_error_enum(d.pop("type"))

        errors = []
        _errors = d.pop("errors")
        for errors_item_data in _errors:

            def _parse_errors_item(
                data: object,
            ) -> (
                ApiV1PricingQuoteAppsPartialUpdateAnnotationsErrorComponent
                | ApiV1PricingQuoteAppsPartialUpdateArchivedAtErrorComponent
                | ApiV1PricingQuoteAppsPartialUpdateArchivedErrorComponent
                | ApiV1PricingQuoteAppsPartialUpdateArchivedReasonErrorComponent
                | ApiV1PricingQuoteAppsPartialUpdateCatalogueAppErrorComponent
                | ApiV1PricingQuoteAppsPartialUpdateCountErrorComponent
                | ApiV1PricingQuoteAppsPartialUpdateCriticalityErrorComponent
                | ApiV1PricingQuoteAppsPartialUpdateDebugModeErrorComponent
                | ApiV1PricingQuoteAppsPartialUpdateDisplayNameErrorComponent
                | ApiV1PricingQuoteAppsPartialUpdateKindErrorComponent
                | ApiV1PricingQuoteAppsPartialUpdateLabelsErrorComponent
                | ApiV1PricingQuoteAppsPartialUpdateNameErrorComponent
                | ApiV1PricingQuoteAppsPartialUpdateNonFieldErrorsErrorComponent
                | ApiV1PricingQuoteAppsPartialUpdatePlatformServiceErrorComponent
                | ApiV1PricingQuoteAppsPartialUpdateProviderErrorComponent
                | ApiV1PricingQuoteAppsPartialUpdateProviderIdErrorComponent
                | ApiV1PricingQuoteAppsPartialUpdateProviderReferenceErrorComponent
                | ApiV1PricingQuoteAppsPartialUpdateQuotedPriceErrorComponent
                | ApiV1PricingQuoteAppsPartialUpdateQuoteWorkspaceErrorComponent
                | ApiV1PricingQuoteAppsPartialUpdateReconciliationEnabledErrorComponent
                | ApiV1PricingQuoteAppsPartialUpdateSlaAvailabilityErrorComponent
                | ApiV1PricingQuoteAppsPartialUpdateSlaTargetErrorComponent
                | ApiV1PricingQuoteAppsPartialUpdateSloAvailabilityErrorComponent
                | ApiV1PricingQuoteAppsPartialUpdateSloTargetErrorComponent
                | ApiV1PricingQuoteAppsPartialUpdateTargetAvailabilityErrorComponent
                | ApiV1PricingQuoteAppsPartialUpdateTolerationsErrorComponent
            ):
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_quote_apps_partial_update_error_type_0 = (
                        ApiV1PricingQuoteAppsPartialUpdateNonFieldErrorsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_quote_apps_partial_update_error_type_0
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_quote_apps_partial_update_error_type_1 = (
                        ApiV1PricingQuoteAppsPartialUpdateNameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_quote_apps_partial_update_error_type_1
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_quote_apps_partial_update_error_type_2 = (
                        ApiV1PricingQuoteAppsPartialUpdateDisplayNameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_quote_apps_partial_update_error_type_2
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_quote_apps_partial_update_error_type_3 = (
                        ApiV1PricingQuoteAppsPartialUpdateLabelsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_quote_apps_partial_update_error_type_3
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_quote_apps_partial_update_error_type_4 = (
                        ApiV1PricingQuoteAppsPartialUpdateAnnotationsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_quote_apps_partial_update_error_type_4
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_quote_apps_partial_update_error_type_5 = (
                        ApiV1PricingQuoteAppsPartialUpdateDebugModeErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_quote_apps_partial_update_error_type_5
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_quote_apps_partial_update_error_type_6 = (
                        ApiV1PricingQuoteAppsPartialUpdateProviderErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_quote_apps_partial_update_error_type_6
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_quote_apps_partial_update_error_type_7 = (
                        ApiV1PricingQuoteAppsPartialUpdateProviderReferenceErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_quote_apps_partial_update_error_type_7
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_quote_apps_partial_update_error_type_8 = (
                        ApiV1PricingQuoteAppsPartialUpdateProviderIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_quote_apps_partial_update_error_type_8
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_quote_apps_partial_update_error_type_9 = (
                        ApiV1PricingQuoteAppsPartialUpdateReconciliationEnabledErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_quote_apps_partial_update_error_type_9
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_quote_apps_partial_update_error_type_10 = (
                        ApiV1PricingQuoteAppsPartialUpdatePlatformServiceErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_quote_apps_partial_update_error_type_10
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_quote_apps_partial_update_error_type_11 = (
                        ApiV1PricingQuoteAppsPartialUpdateKindErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_quote_apps_partial_update_error_type_11
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_quote_apps_partial_update_error_type_12 = (
                        ApiV1PricingQuoteAppsPartialUpdateTolerationsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_quote_apps_partial_update_error_type_12
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_quote_apps_partial_update_error_type_13 = (
                        ApiV1PricingQuoteAppsPartialUpdateArchivedErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_quote_apps_partial_update_error_type_13
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_quote_apps_partial_update_error_type_14 = (
                        ApiV1PricingQuoteAppsPartialUpdateArchivedAtErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_quote_apps_partial_update_error_type_14
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_quote_apps_partial_update_error_type_15 = (
                        ApiV1PricingQuoteAppsPartialUpdateArchivedReasonErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_quote_apps_partial_update_error_type_15
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_quote_apps_partial_update_error_type_16 = (
                        ApiV1PricingQuoteAppsPartialUpdateCriticalityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_quote_apps_partial_update_error_type_16
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_quote_apps_partial_update_error_type_17 = (
                        ApiV1PricingQuoteAppsPartialUpdateTargetAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_quote_apps_partial_update_error_type_17
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_quote_apps_partial_update_error_type_18 = (
                        ApiV1PricingQuoteAppsPartialUpdateSloTargetErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_quote_apps_partial_update_error_type_18
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_quote_apps_partial_update_error_type_19 = (
                        ApiV1PricingQuoteAppsPartialUpdateSloAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_quote_apps_partial_update_error_type_19
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_quote_apps_partial_update_error_type_20 = (
                        ApiV1PricingQuoteAppsPartialUpdateSlaTargetErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_quote_apps_partial_update_error_type_20
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_quote_apps_partial_update_error_type_21 = (
                        ApiV1PricingQuoteAppsPartialUpdateSlaAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_quote_apps_partial_update_error_type_21
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_quote_apps_partial_update_error_type_22 = (
                        ApiV1PricingQuoteAppsPartialUpdateQuoteWorkspaceErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_quote_apps_partial_update_error_type_22
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_quote_apps_partial_update_error_type_23 = (
                        ApiV1PricingQuoteAppsPartialUpdateCatalogueAppErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_quote_apps_partial_update_error_type_23
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_quote_apps_partial_update_error_type_24 = (
                        ApiV1PricingQuoteAppsPartialUpdateCountErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_quote_apps_partial_update_error_type_24
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_api_v1_pricing_quote_apps_partial_update_error_type_25 = (
                    ApiV1PricingQuoteAppsPartialUpdateQuotedPriceErrorComponent.from_dict(data)
                )

                return componentsschemas_api_v1_pricing_quote_apps_partial_update_error_type_25

            errors_item = _parse_errors_item(errors_item_data)

            errors.append(errors_item)

        api_v1_pricing_quote_apps_partial_update_validation_error = cls(
            type_=type_,
            errors=errors,
        )

        api_v1_pricing_quote_apps_partial_update_validation_error.additional_properties = d
        return api_v1_pricing_quote_apps_partial_update_validation_error

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
