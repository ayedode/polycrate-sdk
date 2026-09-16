from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.validation_error_enum import ValidationErrorEnum, check_validation_error_enum

if TYPE_CHECKING:
    from ..models.api_v1_pricing_quote_apps_update_annotations_error_component import (
        ApiV1PricingQuoteAppsUpdateAnnotationsErrorComponent,
    )
    from ..models.api_v1_pricing_quote_apps_update_archived_at_error_component import (
        ApiV1PricingQuoteAppsUpdateArchivedAtErrorComponent,
    )
    from ..models.api_v1_pricing_quote_apps_update_archived_error_component import (
        ApiV1PricingQuoteAppsUpdateArchivedErrorComponent,
    )
    from ..models.api_v1_pricing_quote_apps_update_archived_reason_error_component import (
        ApiV1PricingQuoteAppsUpdateArchivedReasonErrorComponent,
    )
    from ..models.api_v1_pricing_quote_apps_update_catalogue_app_error_component import (
        ApiV1PricingQuoteAppsUpdateCatalogueAppErrorComponent,
    )
    from ..models.api_v1_pricing_quote_apps_update_count_error_component import (
        ApiV1PricingQuoteAppsUpdateCountErrorComponent,
    )
    from ..models.api_v1_pricing_quote_apps_update_criticality_error_component import (
        ApiV1PricingQuoteAppsUpdateCriticalityErrorComponent,
    )
    from ..models.api_v1_pricing_quote_apps_update_debug_mode_error_component import (
        ApiV1PricingQuoteAppsUpdateDebugModeErrorComponent,
    )
    from ..models.api_v1_pricing_quote_apps_update_display_name_error_component import (
        ApiV1PricingQuoteAppsUpdateDisplayNameErrorComponent,
    )
    from ..models.api_v1_pricing_quote_apps_update_kind_error_component import (
        ApiV1PricingQuoteAppsUpdateKindErrorComponent,
    )
    from ..models.api_v1_pricing_quote_apps_update_labels_error_component import (
        ApiV1PricingQuoteAppsUpdateLabelsErrorComponent,
    )
    from ..models.api_v1_pricing_quote_apps_update_name_error_component import (
        ApiV1PricingQuoteAppsUpdateNameErrorComponent,
    )
    from ..models.api_v1_pricing_quote_apps_update_non_field_errors_error_component import (
        ApiV1PricingQuoteAppsUpdateNonFieldErrorsErrorComponent,
    )
    from ..models.api_v1_pricing_quote_apps_update_platform_service_error_component import (
        ApiV1PricingQuoteAppsUpdatePlatformServiceErrorComponent,
    )
    from ..models.api_v1_pricing_quote_apps_update_provider_error_component import (
        ApiV1PricingQuoteAppsUpdateProviderErrorComponent,
    )
    from ..models.api_v1_pricing_quote_apps_update_provider_id_error_component import (
        ApiV1PricingQuoteAppsUpdateProviderIdErrorComponent,
    )
    from ..models.api_v1_pricing_quote_apps_update_provider_reference_error_component import (
        ApiV1PricingQuoteAppsUpdateProviderReferenceErrorComponent,
    )
    from ..models.api_v1_pricing_quote_apps_update_quote_workspace_error_component import (
        ApiV1PricingQuoteAppsUpdateQuoteWorkspaceErrorComponent,
    )
    from ..models.api_v1_pricing_quote_apps_update_quoted_price_error_component import (
        ApiV1PricingQuoteAppsUpdateQuotedPriceErrorComponent,
    )
    from ..models.api_v1_pricing_quote_apps_update_reconciliation_enabled_error_component import (
        ApiV1PricingQuoteAppsUpdateReconciliationEnabledErrorComponent,
    )
    from ..models.api_v1_pricing_quote_apps_update_sla_availability_error_component import (
        ApiV1PricingQuoteAppsUpdateSlaAvailabilityErrorComponent,
    )
    from ..models.api_v1_pricing_quote_apps_update_sla_target_error_component import (
        ApiV1PricingQuoteAppsUpdateSlaTargetErrorComponent,
    )
    from ..models.api_v1_pricing_quote_apps_update_slo_availability_error_component import (
        ApiV1PricingQuoteAppsUpdateSloAvailabilityErrorComponent,
    )
    from ..models.api_v1_pricing_quote_apps_update_slo_target_error_component import (
        ApiV1PricingQuoteAppsUpdateSloTargetErrorComponent,
    )
    from ..models.api_v1_pricing_quote_apps_update_target_availability_error_component import (
        ApiV1PricingQuoteAppsUpdateTargetAvailabilityErrorComponent,
    )
    from ..models.api_v1_pricing_quote_apps_update_tolerations_error_component import (
        ApiV1PricingQuoteAppsUpdateTolerationsErrorComponent,
    )


T = TypeVar("T", bound="ApiV1PricingQuoteAppsUpdateValidationError")


@_attrs_define
class ApiV1PricingQuoteAppsUpdateValidationError:
    """
    Attributes:
        type_ (ValidationErrorEnum): * `validation_error` - Validation Error
        errors (list[ApiV1PricingQuoteAppsUpdateAnnotationsErrorComponent |
            ApiV1PricingQuoteAppsUpdateArchivedAtErrorComponent | ApiV1PricingQuoteAppsUpdateArchivedErrorComponent |
            ApiV1PricingQuoteAppsUpdateArchivedReasonErrorComponent | ApiV1PricingQuoteAppsUpdateCatalogueAppErrorComponent
            | ApiV1PricingQuoteAppsUpdateCountErrorComponent | ApiV1PricingQuoteAppsUpdateCriticalityErrorComponent |
            ApiV1PricingQuoteAppsUpdateDebugModeErrorComponent | ApiV1PricingQuoteAppsUpdateDisplayNameErrorComponent |
            ApiV1PricingQuoteAppsUpdateKindErrorComponent | ApiV1PricingQuoteAppsUpdateLabelsErrorComponent |
            ApiV1PricingQuoteAppsUpdateNameErrorComponent | ApiV1PricingQuoteAppsUpdateNonFieldErrorsErrorComponent |
            ApiV1PricingQuoteAppsUpdatePlatformServiceErrorComponent | ApiV1PricingQuoteAppsUpdateProviderErrorComponent |
            ApiV1PricingQuoteAppsUpdateProviderIdErrorComponent | ApiV1PricingQuoteAppsUpdateProviderReferenceErrorComponent
            | ApiV1PricingQuoteAppsUpdateQuotedPriceErrorComponent | ApiV1PricingQuoteAppsUpdateQuoteWorkspaceErrorComponent
            | ApiV1PricingQuoteAppsUpdateReconciliationEnabledErrorComponent |
            ApiV1PricingQuoteAppsUpdateSlaAvailabilityErrorComponent | ApiV1PricingQuoteAppsUpdateSlaTargetErrorComponent |
            ApiV1PricingQuoteAppsUpdateSloAvailabilityErrorComponent | ApiV1PricingQuoteAppsUpdateSloTargetErrorComponent |
            ApiV1PricingQuoteAppsUpdateTargetAvailabilityErrorComponent |
            ApiV1PricingQuoteAppsUpdateTolerationsErrorComponent]):
    """

    type_: ValidationErrorEnum
    errors: list[
        ApiV1PricingQuoteAppsUpdateAnnotationsErrorComponent
        | ApiV1PricingQuoteAppsUpdateArchivedAtErrorComponent
        | ApiV1PricingQuoteAppsUpdateArchivedErrorComponent
        | ApiV1PricingQuoteAppsUpdateArchivedReasonErrorComponent
        | ApiV1PricingQuoteAppsUpdateCatalogueAppErrorComponent
        | ApiV1PricingQuoteAppsUpdateCountErrorComponent
        | ApiV1PricingQuoteAppsUpdateCriticalityErrorComponent
        | ApiV1PricingQuoteAppsUpdateDebugModeErrorComponent
        | ApiV1PricingQuoteAppsUpdateDisplayNameErrorComponent
        | ApiV1PricingQuoteAppsUpdateKindErrorComponent
        | ApiV1PricingQuoteAppsUpdateLabelsErrorComponent
        | ApiV1PricingQuoteAppsUpdateNameErrorComponent
        | ApiV1PricingQuoteAppsUpdateNonFieldErrorsErrorComponent
        | ApiV1PricingQuoteAppsUpdatePlatformServiceErrorComponent
        | ApiV1PricingQuoteAppsUpdateProviderErrorComponent
        | ApiV1PricingQuoteAppsUpdateProviderIdErrorComponent
        | ApiV1PricingQuoteAppsUpdateProviderReferenceErrorComponent
        | ApiV1PricingQuoteAppsUpdateQuotedPriceErrorComponent
        | ApiV1PricingQuoteAppsUpdateQuoteWorkspaceErrorComponent
        | ApiV1PricingQuoteAppsUpdateReconciliationEnabledErrorComponent
        | ApiV1PricingQuoteAppsUpdateSlaAvailabilityErrorComponent
        | ApiV1PricingQuoteAppsUpdateSlaTargetErrorComponent
        | ApiV1PricingQuoteAppsUpdateSloAvailabilityErrorComponent
        | ApiV1PricingQuoteAppsUpdateSloTargetErrorComponent
        | ApiV1PricingQuoteAppsUpdateTargetAvailabilityErrorComponent
        | ApiV1PricingQuoteAppsUpdateTolerationsErrorComponent
    ]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.api_v1_pricing_quote_apps_update_annotations_error_component import (
            ApiV1PricingQuoteAppsUpdateAnnotationsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_quote_apps_update_archived_at_error_component import (
            ApiV1PricingQuoteAppsUpdateArchivedAtErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_quote_apps_update_archived_error_component import (
            ApiV1PricingQuoteAppsUpdateArchivedErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_quote_apps_update_archived_reason_error_component import (
            ApiV1PricingQuoteAppsUpdateArchivedReasonErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_quote_apps_update_catalogue_app_error_component import (
            ApiV1PricingQuoteAppsUpdateCatalogueAppErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_quote_apps_update_count_error_component import (
            ApiV1PricingQuoteAppsUpdateCountErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_quote_apps_update_criticality_error_component import (
            ApiV1PricingQuoteAppsUpdateCriticalityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_quote_apps_update_debug_mode_error_component import (
            ApiV1PricingQuoteAppsUpdateDebugModeErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_quote_apps_update_display_name_error_component import (
            ApiV1PricingQuoteAppsUpdateDisplayNameErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_quote_apps_update_kind_error_component import (
            ApiV1PricingQuoteAppsUpdateKindErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_quote_apps_update_labels_error_component import (
            ApiV1PricingQuoteAppsUpdateLabelsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_quote_apps_update_name_error_component import (
            ApiV1PricingQuoteAppsUpdateNameErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_quote_apps_update_non_field_errors_error_component import (
            ApiV1PricingQuoteAppsUpdateNonFieldErrorsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_quote_apps_update_platform_service_error_component import (
            ApiV1PricingQuoteAppsUpdatePlatformServiceErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_quote_apps_update_provider_error_component import (
            ApiV1PricingQuoteAppsUpdateProviderErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_quote_apps_update_provider_id_error_component import (
            ApiV1PricingQuoteAppsUpdateProviderIdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_quote_apps_update_provider_reference_error_component import (
            ApiV1PricingQuoteAppsUpdateProviderReferenceErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_quote_apps_update_quote_workspace_error_component import (
            ApiV1PricingQuoteAppsUpdateQuoteWorkspaceErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_quote_apps_update_reconciliation_enabled_error_component import (
            ApiV1PricingQuoteAppsUpdateReconciliationEnabledErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_quote_apps_update_sla_availability_error_component import (
            ApiV1PricingQuoteAppsUpdateSlaAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_quote_apps_update_sla_target_error_component import (
            ApiV1PricingQuoteAppsUpdateSlaTargetErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_quote_apps_update_slo_availability_error_component import (
            ApiV1PricingQuoteAppsUpdateSloAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_quote_apps_update_slo_target_error_component import (
            ApiV1PricingQuoteAppsUpdateSloTargetErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_quote_apps_update_target_availability_error_component import (
            ApiV1PricingQuoteAppsUpdateTargetAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_quote_apps_update_tolerations_error_component import (
            ApiV1PricingQuoteAppsUpdateTolerationsErrorComponent,  # noqa: PLC0415
        )

        type_: str = self.type_

        errors = []
        for errors_item_data in self.errors:
            errors_item: dict[str, Any]
            if isinstance(errors_item_data, ApiV1PricingQuoteAppsUpdateNonFieldErrorsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingQuoteAppsUpdateNameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingQuoteAppsUpdateDisplayNameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingQuoteAppsUpdateLabelsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingQuoteAppsUpdateAnnotationsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingQuoteAppsUpdateDebugModeErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingQuoteAppsUpdateProviderErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingQuoteAppsUpdateProviderReferenceErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingQuoteAppsUpdateProviderIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingQuoteAppsUpdateReconciliationEnabledErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingQuoteAppsUpdatePlatformServiceErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingQuoteAppsUpdateKindErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingQuoteAppsUpdateTolerationsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingQuoteAppsUpdateArchivedErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingQuoteAppsUpdateArchivedAtErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingQuoteAppsUpdateArchivedReasonErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingQuoteAppsUpdateCriticalityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingQuoteAppsUpdateTargetAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingQuoteAppsUpdateSloTargetErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingQuoteAppsUpdateSloAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingQuoteAppsUpdateSlaTargetErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingQuoteAppsUpdateSlaAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingQuoteAppsUpdateQuoteWorkspaceErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingQuoteAppsUpdateCatalogueAppErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingQuoteAppsUpdateCountErrorComponent):
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
        from ..models.api_v1_pricing_quote_apps_update_annotations_error_component import (
            ApiV1PricingQuoteAppsUpdateAnnotationsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_quote_apps_update_archived_at_error_component import (
            ApiV1PricingQuoteAppsUpdateArchivedAtErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_quote_apps_update_archived_error_component import (
            ApiV1PricingQuoteAppsUpdateArchivedErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_quote_apps_update_archived_reason_error_component import (
            ApiV1PricingQuoteAppsUpdateArchivedReasonErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_quote_apps_update_catalogue_app_error_component import (
            ApiV1PricingQuoteAppsUpdateCatalogueAppErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_quote_apps_update_count_error_component import (
            ApiV1PricingQuoteAppsUpdateCountErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_quote_apps_update_criticality_error_component import (
            ApiV1PricingQuoteAppsUpdateCriticalityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_quote_apps_update_debug_mode_error_component import (
            ApiV1PricingQuoteAppsUpdateDebugModeErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_quote_apps_update_display_name_error_component import (
            ApiV1PricingQuoteAppsUpdateDisplayNameErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_quote_apps_update_kind_error_component import (
            ApiV1PricingQuoteAppsUpdateKindErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_quote_apps_update_labels_error_component import (
            ApiV1PricingQuoteAppsUpdateLabelsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_quote_apps_update_name_error_component import (
            ApiV1PricingQuoteAppsUpdateNameErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_quote_apps_update_non_field_errors_error_component import (
            ApiV1PricingQuoteAppsUpdateNonFieldErrorsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_quote_apps_update_platform_service_error_component import (
            ApiV1PricingQuoteAppsUpdatePlatformServiceErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_quote_apps_update_provider_error_component import (
            ApiV1PricingQuoteAppsUpdateProviderErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_quote_apps_update_provider_id_error_component import (
            ApiV1PricingQuoteAppsUpdateProviderIdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_quote_apps_update_provider_reference_error_component import (
            ApiV1PricingQuoteAppsUpdateProviderReferenceErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_quote_apps_update_quote_workspace_error_component import (
            ApiV1PricingQuoteAppsUpdateQuoteWorkspaceErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_quote_apps_update_quoted_price_error_component import (
            ApiV1PricingQuoteAppsUpdateQuotedPriceErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_quote_apps_update_reconciliation_enabled_error_component import (
            ApiV1PricingQuoteAppsUpdateReconciliationEnabledErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_quote_apps_update_sla_availability_error_component import (
            ApiV1PricingQuoteAppsUpdateSlaAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_quote_apps_update_sla_target_error_component import (
            ApiV1PricingQuoteAppsUpdateSlaTargetErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_quote_apps_update_slo_availability_error_component import (
            ApiV1PricingQuoteAppsUpdateSloAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_quote_apps_update_slo_target_error_component import (
            ApiV1PricingQuoteAppsUpdateSloTargetErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_quote_apps_update_target_availability_error_component import (
            ApiV1PricingQuoteAppsUpdateTargetAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_quote_apps_update_tolerations_error_component import (
            ApiV1PricingQuoteAppsUpdateTolerationsErrorComponent,  # noqa: PLC0415
        )

        d = dict(src_dict)
        type_ = check_validation_error_enum(d.pop("type"))

        errors = []
        _errors = d.pop("errors")
        for errors_item_data in _errors:

            def _parse_errors_item(
                data: object,
            ) -> (
                ApiV1PricingQuoteAppsUpdateAnnotationsErrorComponent
                | ApiV1PricingQuoteAppsUpdateArchivedAtErrorComponent
                | ApiV1PricingQuoteAppsUpdateArchivedErrorComponent
                | ApiV1PricingQuoteAppsUpdateArchivedReasonErrorComponent
                | ApiV1PricingQuoteAppsUpdateCatalogueAppErrorComponent
                | ApiV1PricingQuoteAppsUpdateCountErrorComponent
                | ApiV1PricingQuoteAppsUpdateCriticalityErrorComponent
                | ApiV1PricingQuoteAppsUpdateDebugModeErrorComponent
                | ApiV1PricingQuoteAppsUpdateDisplayNameErrorComponent
                | ApiV1PricingQuoteAppsUpdateKindErrorComponent
                | ApiV1PricingQuoteAppsUpdateLabelsErrorComponent
                | ApiV1PricingQuoteAppsUpdateNameErrorComponent
                | ApiV1PricingQuoteAppsUpdateNonFieldErrorsErrorComponent
                | ApiV1PricingQuoteAppsUpdatePlatformServiceErrorComponent
                | ApiV1PricingQuoteAppsUpdateProviderErrorComponent
                | ApiV1PricingQuoteAppsUpdateProviderIdErrorComponent
                | ApiV1PricingQuoteAppsUpdateProviderReferenceErrorComponent
                | ApiV1PricingQuoteAppsUpdateQuotedPriceErrorComponent
                | ApiV1PricingQuoteAppsUpdateQuoteWorkspaceErrorComponent
                | ApiV1PricingQuoteAppsUpdateReconciliationEnabledErrorComponent
                | ApiV1PricingQuoteAppsUpdateSlaAvailabilityErrorComponent
                | ApiV1PricingQuoteAppsUpdateSlaTargetErrorComponent
                | ApiV1PricingQuoteAppsUpdateSloAvailabilityErrorComponent
                | ApiV1PricingQuoteAppsUpdateSloTargetErrorComponent
                | ApiV1PricingQuoteAppsUpdateTargetAvailabilityErrorComponent
                | ApiV1PricingQuoteAppsUpdateTolerationsErrorComponent
            ):
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_quote_apps_update_error_type_0 = (
                        ApiV1PricingQuoteAppsUpdateNonFieldErrorsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_quote_apps_update_error_type_0
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_quote_apps_update_error_type_1 = (
                        ApiV1PricingQuoteAppsUpdateNameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_quote_apps_update_error_type_1
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_quote_apps_update_error_type_2 = (
                        ApiV1PricingQuoteAppsUpdateDisplayNameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_quote_apps_update_error_type_2
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_quote_apps_update_error_type_3 = (
                        ApiV1PricingQuoteAppsUpdateLabelsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_quote_apps_update_error_type_3
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_quote_apps_update_error_type_4 = (
                        ApiV1PricingQuoteAppsUpdateAnnotationsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_quote_apps_update_error_type_4
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_quote_apps_update_error_type_5 = (
                        ApiV1PricingQuoteAppsUpdateDebugModeErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_quote_apps_update_error_type_5
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_quote_apps_update_error_type_6 = (
                        ApiV1PricingQuoteAppsUpdateProviderErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_quote_apps_update_error_type_6
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_quote_apps_update_error_type_7 = (
                        ApiV1PricingQuoteAppsUpdateProviderReferenceErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_quote_apps_update_error_type_7
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_quote_apps_update_error_type_8 = (
                        ApiV1PricingQuoteAppsUpdateProviderIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_quote_apps_update_error_type_8
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_quote_apps_update_error_type_9 = (
                        ApiV1PricingQuoteAppsUpdateReconciliationEnabledErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_quote_apps_update_error_type_9
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_quote_apps_update_error_type_10 = (
                        ApiV1PricingQuoteAppsUpdatePlatformServiceErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_quote_apps_update_error_type_10
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_quote_apps_update_error_type_11 = (
                        ApiV1PricingQuoteAppsUpdateKindErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_quote_apps_update_error_type_11
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_quote_apps_update_error_type_12 = (
                        ApiV1PricingQuoteAppsUpdateTolerationsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_quote_apps_update_error_type_12
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_quote_apps_update_error_type_13 = (
                        ApiV1PricingQuoteAppsUpdateArchivedErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_quote_apps_update_error_type_13
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_quote_apps_update_error_type_14 = (
                        ApiV1PricingQuoteAppsUpdateArchivedAtErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_quote_apps_update_error_type_14
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_quote_apps_update_error_type_15 = (
                        ApiV1PricingQuoteAppsUpdateArchivedReasonErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_quote_apps_update_error_type_15
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_quote_apps_update_error_type_16 = (
                        ApiV1PricingQuoteAppsUpdateCriticalityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_quote_apps_update_error_type_16
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_quote_apps_update_error_type_17 = (
                        ApiV1PricingQuoteAppsUpdateTargetAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_quote_apps_update_error_type_17
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_quote_apps_update_error_type_18 = (
                        ApiV1PricingQuoteAppsUpdateSloTargetErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_quote_apps_update_error_type_18
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_quote_apps_update_error_type_19 = (
                        ApiV1PricingQuoteAppsUpdateSloAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_quote_apps_update_error_type_19
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_quote_apps_update_error_type_20 = (
                        ApiV1PricingQuoteAppsUpdateSlaTargetErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_quote_apps_update_error_type_20
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_quote_apps_update_error_type_21 = (
                        ApiV1PricingQuoteAppsUpdateSlaAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_quote_apps_update_error_type_21
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_quote_apps_update_error_type_22 = (
                        ApiV1PricingQuoteAppsUpdateQuoteWorkspaceErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_quote_apps_update_error_type_22
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_quote_apps_update_error_type_23 = (
                        ApiV1PricingQuoteAppsUpdateCatalogueAppErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_quote_apps_update_error_type_23
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_quote_apps_update_error_type_24 = (
                        ApiV1PricingQuoteAppsUpdateCountErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_quote_apps_update_error_type_24
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_api_v1_pricing_quote_apps_update_error_type_25 = (
                    ApiV1PricingQuoteAppsUpdateQuotedPriceErrorComponent.from_dict(data)
                )

                return componentsschemas_api_v1_pricing_quote_apps_update_error_type_25

            errors_item = _parse_errors_item(errors_item_data)

            errors.append(errors_item)

        api_v1_pricing_quote_apps_update_validation_error = cls(
            type_=type_,
            errors=errors,
        )

        api_v1_pricing_quote_apps_update_validation_error.additional_properties = d
        return api_v1_pricing_quote_apps_update_validation_error

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
