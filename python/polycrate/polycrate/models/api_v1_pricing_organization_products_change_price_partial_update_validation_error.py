from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.validation_error_enum import ValidationErrorEnum, check_validation_error_enum

if TYPE_CHECKING:
    from ..models.api_v1_pricing_organization_products_change_price_partial_update_active_from_error_component import (
        ApiV1PricingOrganizationProductsChangePricePartialUpdateActiveFromErrorComponent,
    )
    from ..models.api_v1_pricing_organization_products_change_price_partial_update_active_until_error_component import (
        ApiV1PricingOrganizationProductsChangePricePartialUpdateActiveUntilErrorComponent,
    )
    from ..models.api_v1_pricing_organization_products_change_price_partial_update_agreed_price_error_component import (
        ApiV1PricingOrganizationProductsChangePricePartialUpdateAgreedPriceErrorComponent,
    )
    from ..models.api_v1_pricing_organization_products_change_price_partial_update_agreed_price_reason_error_component import (
        ApiV1PricingOrganizationProductsChangePricePartialUpdateAgreedPriceReasonErrorComponent,
    )
    from ..models.api_v1_pricing_organization_products_change_price_partial_update_annotations_error_component import (
        ApiV1PricingOrganizationProductsChangePricePartialUpdateAnnotationsErrorComponent,
    )
    from ..models.api_v1_pricing_organization_products_change_price_partial_update_archived_at_error_component import (
        ApiV1PricingOrganizationProductsChangePricePartialUpdateArchivedAtErrorComponent,
    )
    from ..models.api_v1_pricing_organization_products_change_price_partial_update_archived_error_component import (
        ApiV1PricingOrganizationProductsChangePricePartialUpdateArchivedErrorComponent,
    )
    from ..models.api_v1_pricing_organization_products_change_price_partial_update_archived_reason_error_component import (
        ApiV1PricingOrganizationProductsChangePricePartialUpdateArchivedReasonErrorComponent,
    )
    from ..models.api_v1_pricing_organization_products_change_price_partial_update_auto_managed_error_component import (
        ApiV1PricingOrganizationProductsChangePricePartialUpdateAutoManagedErrorComponent,
    )
    from ..models.api_v1_pricing_organization_products_change_price_partial_update_catalogue_app_error_component import (
        ApiV1PricingOrganizationProductsChangePricePartialUpdateCatalogueAppErrorComponent,
    )
    from ..models.api_v1_pricing_organization_products_change_price_partial_update_content_type_error_component import (
        ApiV1PricingOrganizationProductsChangePricePartialUpdateContentTypeErrorComponent,
    )
    from ..models.api_v1_pricing_organization_products_change_price_partial_update_criticality_error_component import (
        ApiV1PricingOrganizationProductsChangePricePartialUpdateCriticalityErrorComponent,
    )
    from ..models.api_v1_pricing_organization_products_change_price_partial_update_debug_mode_error_component import (
        ApiV1PricingOrganizationProductsChangePricePartialUpdateDebugModeErrorComponent,
    )
    from ..models.api_v1_pricing_organization_products_change_price_partial_update_display_name_error_component import (
        ApiV1PricingOrganizationProductsChangePricePartialUpdateDisplayNameErrorComponent,
    )
    from ..models.api_v1_pricing_organization_products_change_price_partial_update_internal_note_error_component import (
        ApiV1PricingOrganizationProductsChangePricePartialUpdateInternalNoteErrorComponent,
    )
    from ..models.api_v1_pricing_organization_products_change_price_partial_update_kind_error_component import (
        ApiV1PricingOrganizationProductsChangePricePartialUpdateKindErrorComponent,
    )
    from ..models.api_v1_pricing_organization_products_change_price_partial_update_labels_error_component import (
        ApiV1PricingOrganizationProductsChangePricePartialUpdateLabelsErrorComponent,
    )
    from ..models.api_v1_pricing_organization_products_change_price_partial_update_name_error_component import (
        ApiV1PricingOrganizationProductsChangePricePartialUpdateNameErrorComponent,
    )
    from ..models.api_v1_pricing_organization_products_change_price_partial_update_non_field_errors_error_component import (
        ApiV1PricingOrganizationProductsChangePricePartialUpdateNonFieldErrorsErrorComponent,
    )
    from ..models.api_v1_pricing_organization_products_change_price_partial_update_object_id_error_component import (
        ApiV1PricingOrganizationProductsChangePricePartialUpdateObjectIdErrorComponent,
    )
    from ..models.api_v1_pricing_organization_products_change_price_partial_update_platform_service_error_component import (
        ApiV1PricingOrganizationProductsChangePricePartialUpdatePlatformServiceErrorComponent,
    )
    from ..models.api_v1_pricing_organization_products_change_price_partial_update_provider_error_component import (
        ApiV1PricingOrganizationProductsChangePricePartialUpdateProviderErrorComponent,
    )
    from ..models.api_v1_pricing_organization_products_change_price_partial_update_provider_id_error_component import (
        ApiV1PricingOrganizationProductsChangePricePartialUpdateProviderIdErrorComponent,
    )
    from ..models.api_v1_pricing_organization_products_change_price_partial_update_provider_reference_error_component import (
        ApiV1PricingOrganizationProductsChangePricePartialUpdateProviderReferenceErrorComponent,
    )
    from ..models.api_v1_pricing_organization_products_change_price_partial_update_reconciliation_enabled_error_component import (
        ApiV1PricingOrganizationProductsChangePricePartialUpdateReconciliationEnabledErrorComponent,
    )
    from ..models.api_v1_pricing_organization_products_change_price_partial_update_sla_availability_error_component import (
        ApiV1PricingOrganizationProductsChangePricePartialUpdateSlaAvailabilityErrorComponent,
    )
    from ..models.api_v1_pricing_organization_products_change_price_partial_update_sla_target_error_component import (
        ApiV1PricingOrganizationProductsChangePricePartialUpdateSlaTargetErrorComponent,
    )
    from ..models.api_v1_pricing_organization_products_change_price_partial_update_slo_availability_error_component import (
        ApiV1PricingOrganizationProductsChangePricePartialUpdateSloAvailabilityErrorComponent,
    )
    from ..models.api_v1_pricing_organization_products_change_price_partial_update_slo_target_error_component import (
        ApiV1PricingOrganizationProductsChangePricePartialUpdateSloTargetErrorComponent,
    )
    from ..models.api_v1_pricing_organization_products_change_price_partial_update_target_availability_error_component import (
        ApiV1PricingOrganizationProductsChangePricePartialUpdateTargetAvailabilityErrorComponent,
    )
    from ..models.api_v1_pricing_organization_products_change_price_partial_update_tolerations_error_component import (
        ApiV1PricingOrganizationProductsChangePricePartialUpdateTolerationsErrorComponent,
    )


T = TypeVar("T", bound="ApiV1PricingOrganizationProductsChangePricePartialUpdateValidationError")


@_attrs_define
class ApiV1PricingOrganizationProductsChangePricePartialUpdateValidationError:
    """
    Attributes:
        type_ (ValidationErrorEnum): * `validation_error` - Validation Error
        errors (list[ApiV1PricingOrganizationProductsChangePricePartialUpdateActiveFromErrorComponent |
            ApiV1PricingOrganizationProductsChangePricePartialUpdateActiveUntilErrorComponent |
            ApiV1PricingOrganizationProductsChangePricePartialUpdateAgreedPriceErrorComponent |
            ApiV1PricingOrganizationProductsChangePricePartialUpdateAgreedPriceReasonErrorComponent |
            ApiV1PricingOrganizationProductsChangePricePartialUpdateAnnotationsErrorComponent |
            ApiV1PricingOrganizationProductsChangePricePartialUpdateArchivedAtErrorComponent |
            ApiV1PricingOrganizationProductsChangePricePartialUpdateArchivedErrorComponent |
            ApiV1PricingOrganizationProductsChangePricePartialUpdateArchivedReasonErrorComponent |
            ApiV1PricingOrganizationProductsChangePricePartialUpdateAutoManagedErrorComponent |
            ApiV1PricingOrganizationProductsChangePricePartialUpdateCatalogueAppErrorComponent |
            ApiV1PricingOrganizationProductsChangePricePartialUpdateContentTypeErrorComponent |
            ApiV1PricingOrganizationProductsChangePricePartialUpdateCriticalityErrorComponent |
            ApiV1PricingOrganizationProductsChangePricePartialUpdateDebugModeErrorComponent |
            ApiV1PricingOrganizationProductsChangePricePartialUpdateDisplayNameErrorComponent |
            ApiV1PricingOrganizationProductsChangePricePartialUpdateInternalNoteErrorComponent |
            ApiV1PricingOrganizationProductsChangePricePartialUpdateKindErrorComponent |
            ApiV1PricingOrganizationProductsChangePricePartialUpdateLabelsErrorComponent |
            ApiV1PricingOrganizationProductsChangePricePartialUpdateNameErrorComponent |
            ApiV1PricingOrganizationProductsChangePricePartialUpdateNonFieldErrorsErrorComponent |
            ApiV1PricingOrganizationProductsChangePricePartialUpdateObjectIdErrorComponent |
            ApiV1PricingOrganizationProductsChangePricePartialUpdatePlatformServiceErrorComponent |
            ApiV1PricingOrganizationProductsChangePricePartialUpdateProviderErrorComponent |
            ApiV1PricingOrganizationProductsChangePricePartialUpdateProviderIdErrorComponent |
            ApiV1PricingOrganizationProductsChangePricePartialUpdateProviderReferenceErrorComponent |
            ApiV1PricingOrganizationProductsChangePricePartialUpdateReconciliationEnabledErrorComponent |
            ApiV1PricingOrganizationProductsChangePricePartialUpdateSlaAvailabilityErrorComponent |
            ApiV1PricingOrganizationProductsChangePricePartialUpdateSlaTargetErrorComponent |
            ApiV1PricingOrganizationProductsChangePricePartialUpdateSloAvailabilityErrorComponent |
            ApiV1PricingOrganizationProductsChangePricePartialUpdateSloTargetErrorComponent |
            ApiV1PricingOrganizationProductsChangePricePartialUpdateTargetAvailabilityErrorComponent |
            ApiV1PricingOrganizationProductsChangePricePartialUpdateTolerationsErrorComponent]):
    """

    type_: ValidationErrorEnum
    errors: list[
        ApiV1PricingOrganizationProductsChangePricePartialUpdateActiveFromErrorComponent
        | ApiV1PricingOrganizationProductsChangePricePartialUpdateActiveUntilErrorComponent
        | ApiV1PricingOrganizationProductsChangePricePartialUpdateAgreedPriceErrorComponent
        | ApiV1PricingOrganizationProductsChangePricePartialUpdateAgreedPriceReasonErrorComponent
        | ApiV1PricingOrganizationProductsChangePricePartialUpdateAnnotationsErrorComponent
        | ApiV1PricingOrganizationProductsChangePricePartialUpdateArchivedAtErrorComponent
        | ApiV1PricingOrganizationProductsChangePricePartialUpdateArchivedErrorComponent
        | ApiV1PricingOrganizationProductsChangePricePartialUpdateArchivedReasonErrorComponent
        | ApiV1PricingOrganizationProductsChangePricePartialUpdateAutoManagedErrorComponent
        | ApiV1PricingOrganizationProductsChangePricePartialUpdateCatalogueAppErrorComponent
        | ApiV1PricingOrganizationProductsChangePricePartialUpdateContentTypeErrorComponent
        | ApiV1PricingOrganizationProductsChangePricePartialUpdateCriticalityErrorComponent
        | ApiV1PricingOrganizationProductsChangePricePartialUpdateDebugModeErrorComponent
        | ApiV1PricingOrganizationProductsChangePricePartialUpdateDisplayNameErrorComponent
        | ApiV1PricingOrganizationProductsChangePricePartialUpdateInternalNoteErrorComponent
        | ApiV1PricingOrganizationProductsChangePricePartialUpdateKindErrorComponent
        | ApiV1PricingOrganizationProductsChangePricePartialUpdateLabelsErrorComponent
        | ApiV1PricingOrganizationProductsChangePricePartialUpdateNameErrorComponent
        | ApiV1PricingOrganizationProductsChangePricePartialUpdateNonFieldErrorsErrorComponent
        | ApiV1PricingOrganizationProductsChangePricePartialUpdateObjectIdErrorComponent
        | ApiV1PricingOrganizationProductsChangePricePartialUpdatePlatformServiceErrorComponent
        | ApiV1PricingOrganizationProductsChangePricePartialUpdateProviderErrorComponent
        | ApiV1PricingOrganizationProductsChangePricePartialUpdateProviderIdErrorComponent
        | ApiV1PricingOrganizationProductsChangePricePartialUpdateProviderReferenceErrorComponent
        | ApiV1PricingOrganizationProductsChangePricePartialUpdateReconciliationEnabledErrorComponent
        | ApiV1PricingOrganizationProductsChangePricePartialUpdateSlaAvailabilityErrorComponent
        | ApiV1PricingOrganizationProductsChangePricePartialUpdateSlaTargetErrorComponent
        | ApiV1PricingOrganizationProductsChangePricePartialUpdateSloAvailabilityErrorComponent
        | ApiV1PricingOrganizationProductsChangePricePartialUpdateSloTargetErrorComponent
        | ApiV1PricingOrganizationProductsChangePricePartialUpdateTargetAvailabilityErrorComponent
        | ApiV1PricingOrganizationProductsChangePricePartialUpdateTolerationsErrorComponent
    ]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.api_v1_pricing_organization_products_change_price_partial_update_active_from_error_component import (
            ApiV1PricingOrganizationProductsChangePricePartialUpdateActiveFromErrorComponent,
        )
        from ..models.api_v1_pricing_organization_products_change_price_partial_update_active_until_error_component import (
            ApiV1PricingOrganizationProductsChangePricePartialUpdateActiveUntilErrorComponent,
        )
        from ..models.api_v1_pricing_organization_products_change_price_partial_update_agreed_price_error_component import (
            ApiV1PricingOrganizationProductsChangePricePartialUpdateAgreedPriceErrorComponent,
        )
        from ..models.api_v1_pricing_organization_products_change_price_partial_update_agreed_price_reason_error_component import (
            ApiV1PricingOrganizationProductsChangePricePartialUpdateAgreedPriceReasonErrorComponent,
        )
        from ..models.api_v1_pricing_organization_products_change_price_partial_update_annotations_error_component import (
            ApiV1PricingOrganizationProductsChangePricePartialUpdateAnnotationsErrorComponent,
        )
        from ..models.api_v1_pricing_organization_products_change_price_partial_update_archived_at_error_component import (
            ApiV1PricingOrganizationProductsChangePricePartialUpdateArchivedAtErrorComponent,
        )
        from ..models.api_v1_pricing_organization_products_change_price_partial_update_archived_error_component import (
            ApiV1PricingOrganizationProductsChangePricePartialUpdateArchivedErrorComponent,
        )
        from ..models.api_v1_pricing_organization_products_change_price_partial_update_archived_reason_error_component import (
            ApiV1PricingOrganizationProductsChangePricePartialUpdateArchivedReasonErrorComponent,
        )
        from ..models.api_v1_pricing_organization_products_change_price_partial_update_auto_managed_error_component import (
            ApiV1PricingOrganizationProductsChangePricePartialUpdateAutoManagedErrorComponent,
        )
        from ..models.api_v1_pricing_organization_products_change_price_partial_update_catalogue_app_error_component import (
            ApiV1PricingOrganizationProductsChangePricePartialUpdateCatalogueAppErrorComponent,
        )
        from ..models.api_v1_pricing_organization_products_change_price_partial_update_content_type_error_component import (
            ApiV1PricingOrganizationProductsChangePricePartialUpdateContentTypeErrorComponent,
        )
        from ..models.api_v1_pricing_organization_products_change_price_partial_update_criticality_error_component import (
            ApiV1PricingOrganizationProductsChangePricePartialUpdateCriticalityErrorComponent,
        )
        from ..models.api_v1_pricing_organization_products_change_price_partial_update_debug_mode_error_component import (
            ApiV1PricingOrganizationProductsChangePricePartialUpdateDebugModeErrorComponent,
        )
        from ..models.api_v1_pricing_organization_products_change_price_partial_update_display_name_error_component import (
            ApiV1PricingOrganizationProductsChangePricePartialUpdateDisplayNameErrorComponent,
        )
        from ..models.api_v1_pricing_organization_products_change_price_partial_update_kind_error_component import (
            ApiV1PricingOrganizationProductsChangePricePartialUpdateKindErrorComponent,
        )
        from ..models.api_v1_pricing_organization_products_change_price_partial_update_labels_error_component import (
            ApiV1PricingOrganizationProductsChangePricePartialUpdateLabelsErrorComponent,
        )
        from ..models.api_v1_pricing_organization_products_change_price_partial_update_name_error_component import (
            ApiV1PricingOrganizationProductsChangePricePartialUpdateNameErrorComponent,
        )
        from ..models.api_v1_pricing_organization_products_change_price_partial_update_non_field_errors_error_component import (
            ApiV1PricingOrganizationProductsChangePricePartialUpdateNonFieldErrorsErrorComponent,
        )
        from ..models.api_v1_pricing_organization_products_change_price_partial_update_object_id_error_component import (
            ApiV1PricingOrganizationProductsChangePricePartialUpdateObjectIdErrorComponent,
        )
        from ..models.api_v1_pricing_organization_products_change_price_partial_update_platform_service_error_component import (
            ApiV1PricingOrganizationProductsChangePricePartialUpdatePlatformServiceErrorComponent,
        )
        from ..models.api_v1_pricing_organization_products_change_price_partial_update_provider_error_component import (
            ApiV1PricingOrganizationProductsChangePricePartialUpdateProviderErrorComponent,
        )
        from ..models.api_v1_pricing_organization_products_change_price_partial_update_provider_id_error_component import (
            ApiV1PricingOrganizationProductsChangePricePartialUpdateProviderIdErrorComponent,
        )
        from ..models.api_v1_pricing_organization_products_change_price_partial_update_provider_reference_error_component import (
            ApiV1PricingOrganizationProductsChangePricePartialUpdateProviderReferenceErrorComponent,
        )
        from ..models.api_v1_pricing_organization_products_change_price_partial_update_reconciliation_enabled_error_component import (
            ApiV1PricingOrganizationProductsChangePricePartialUpdateReconciliationEnabledErrorComponent,
        )
        from ..models.api_v1_pricing_organization_products_change_price_partial_update_sla_availability_error_component import (
            ApiV1PricingOrganizationProductsChangePricePartialUpdateSlaAvailabilityErrorComponent,
        )
        from ..models.api_v1_pricing_organization_products_change_price_partial_update_sla_target_error_component import (
            ApiV1PricingOrganizationProductsChangePricePartialUpdateSlaTargetErrorComponent,
        )
        from ..models.api_v1_pricing_organization_products_change_price_partial_update_slo_availability_error_component import (
            ApiV1PricingOrganizationProductsChangePricePartialUpdateSloAvailabilityErrorComponent,
        )
        from ..models.api_v1_pricing_organization_products_change_price_partial_update_slo_target_error_component import (
            ApiV1PricingOrganizationProductsChangePricePartialUpdateSloTargetErrorComponent,
        )
        from ..models.api_v1_pricing_organization_products_change_price_partial_update_target_availability_error_component import (
            ApiV1PricingOrganizationProductsChangePricePartialUpdateTargetAvailabilityErrorComponent,
        )
        from ..models.api_v1_pricing_organization_products_change_price_partial_update_tolerations_error_component import (
            ApiV1PricingOrganizationProductsChangePricePartialUpdateTolerationsErrorComponent,
        )

        type_: str = self.type_

        errors = []
        for errors_item_data in self.errors:
            errors_item: dict[str, Any]
            if isinstance(
                errors_item_data, ApiV1PricingOrganizationProductsChangePricePartialUpdateNonFieldErrorsErrorComponent
            ):
                errors_item = errors_item_data.to_dict()
            elif isinstance(
                errors_item_data, ApiV1PricingOrganizationProductsChangePricePartialUpdateNameErrorComponent
            ):
                errors_item = errors_item_data.to_dict()
            elif isinstance(
                errors_item_data, ApiV1PricingOrganizationProductsChangePricePartialUpdateDisplayNameErrorComponent
            ):
                errors_item = errors_item_data.to_dict()
            elif isinstance(
                errors_item_data, ApiV1PricingOrganizationProductsChangePricePartialUpdateLabelsErrorComponent
            ):
                errors_item = errors_item_data.to_dict()
            elif isinstance(
                errors_item_data, ApiV1PricingOrganizationProductsChangePricePartialUpdateAnnotationsErrorComponent
            ):
                errors_item = errors_item_data.to_dict()
            elif isinstance(
                errors_item_data, ApiV1PricingOrganizationProductsChangePricePartialUpdateDebugModeErrorComponent
            ):
                errors_item = errors_item_data.to_dict()
            elif isinstance(
                errors_item_data, ApiV1PricingOrganizationProductsChangePricePartialUpdateProviderErrorComponent
            ):
                errors_item = errors_item_data.to_dict()
            elif isinstance(
                errors_item_data,
                ApiV1PricingOrganizationProductsChangePricePartialUpdateProviderReferenceErrorComponent,
            ):
                errors_item = errors_item_data.to_dict()
            elif isinstance(
                errors_item_data, ApiV1PricingOrganizationProductsChangePricePartialUpdateProviderIdErrorComponent
            ):
                errors_item = errors_item_data.to_dict()
            elif isinstance(
                errors_item_data,
                ApiV1PricingOrganizationProductsChangePricePartialUpdateReconciliationEnabledErrorComponent,
            ):
                errors_item = errors_item_data.to_dict()
            elif isinstance(
                errors_item_data, ApiV1PricingOrganizationProductsChangePricePartialUpdatePlatformServiceErrorComponent
            ):
                errors_item = errors_item_data.to_dict()
            elif isinstance(
                errors_item_data, ApiV1PricingOrganizationProductsChangePricePartialUpdateKindErrorComponent
            ):
                errors_item = errors_item_data.to_dict()
            elif isinstance(
                errors_item_data, ApiV1PricingOrganizationProductsChangePricePartialUpdateTolerationsErrorComponent
            ):
                errors_item = errors_item_data.to_dict()
            elif isinstance(
                errors_item_data, ApiV1PricingOrganizationProductsChangePricePartialUpdateArchivedErrorComponent
            ):
                errors_item = errors_item_data.to_dict()
            elif isinstance(
                errors_item_data, ApiV1PricingOrganizationProductsChangePricePartialUpdateArchivedAtErrorComponent
            ):
                errors_item = errors_item_data.to_dict()
            elif isinstance(
                errors_item_data, ApiV1PricingOrganizationProductsChangePricePartialUpdateArchivedReasonErrorComponent
            ):
                errors_item = errors_item_data.to_dict()
            elif isinstance(
                errors_item_data, ApiV1PricingOrganizationProductsChangePricePartialUpdateCriticalityErrorComponent
            ):
                errors_item = errors_item_data.to_dict()
            elif isinstance(
                errors_item_data,
                ApiV1PricingOrganizationProductsChangePricePartialUpdateTargetAvailabilityErrorComponent,
            ):
                errors_item = errors_item_data.to_dict()
            elif isinstance(
                errors_item_data, ApiV1PricingOrganizationProductsChangePricePartialUpdateSloTargetErrorComponent
            ):
                errors_item = errors_item_data.to_dict()
            elif isinstance(
                errors_item_data, ApiV1PricingOrganizationProductsChangePricePartialUpdateSloAvailabilityErrorComponent
            ):
                errors_item = errors_item_data.to_dict()
            elif isinstance(
                errors_item_data, ApiV1PricingOrganizationProductsChangePricePartialUpdateSlaTargetErrorComponent
            ):
                errors_item = errors_item_data.to_dict()
            elif isinstance(
                errors_item_data, ApiV1PricingOrganizationProductsChangePricePartialUpdateSlaAvailabilityErrorComponent
            ):
                errors_item = errors_item_data.to_dict()
            elif isinstance(
                errors_item_data, ApiV1PricingOrganizationProductsChangePricePartialUpdateCatalogueAppErrorComponent
            ):
                errors_item = errors_item_data.to_dict()
            elif isinstance(
                errors_item_data, ApiV1PricingOrganizationProductsChangePricePartialUpdateContentTypeErrorComponent
            ):
                errors_item = errors_item_data.to_dict()
            elif isinstance(
                errors_item_data, ApiV1PricingOrganizationProductsChangePricePartialUpdateObjectIdErrorComponent
            ):
                errors_item = errors_item_data.to_dict()
            elif isinstance(
                errors_item_data, ApiV1PricingOrganizationProductsChangePricePartialUpdateAutoManagedErrorComponent
            ):
                errors_item = errors_item_data.to_dict()
            elif isinstance(
                errors_item_data, ApiV1PricingOrganizationProductsChangePricePartialUpdateActiveFromErrorComponent
            ):
                errors_item = errors_item_data.to_dict()
            elif isinstance(
                errors_item_data, ApiV1PricingOrganizationProductsChangePricePartialUpdateActiveUntilErrorComponent
            ):
                errors_item = errors_item_data.to_dict()
            elif isinstance(
                errors_item_data, ApiV1PricingOrganizationProductsChangePricePartialUpdateAgreedPriceErrorComponent
            ):
                errors_item = errors_item_data.to_dict()
            elif isinstance(
                errors_item_data,
                ApiV1PricingOrganizationProductsChangePricePartialUpdateAgreedPriceReasonErrorComponent,
            ):
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
        from ..models.api_v1_pricing_organization_products_change_price_partial_update_active_from_error_component import (
            ApiV1PricingOrganizationProductsChangePricePartialUpdateActiveFromErrorComponent,
        )
        from ..models.api_v1_pricing_organization_products_change_price_partial_update_active_until_error_component import (
            ApiV1PricingOrganizationProductsChangePricePartialUpdateActiveUntilErrorComponent,
        )
        from ..models.api_v1_pricing_organization_products_change_price_partial_update_agreed_price_error_component import (
            ApiV1PricingOrganizationProductsChangePricePartialUpdateAgreedPriceErrorComponent,
        )
        from ..models.api_v1_pricing_organization_products_change_price_partial_update_agreed_price_reason_error_component import (
            ApiV1PricingOrganizationProductsChangePricePartialUpdateAgreedPriceReasonErrorComponent,
        )
        from ..models.api_v1_pricing_organization_products_change_price_partial_update_annotations_error_component import (
            ApiV1PricingOrganizationProductsChangePricePartialUpdateAnnotationsErrorComponent,
        )
        from ..models.api_v1_pricing_organization_products_change_price_partial_update_archived_at_error_component import (
            ApiV1PricingOrganizationProductsChangePricePartialUpdateArchivedAtErrorComponent,
        )
        from ..models.api_v1_pricing_organization_products_change_price_partial_update_archived_error_component import (
            ApiV1PricingOrganizationProductsChangePricePartialUpdateArchivedErrorComponent,
        )
        from ..models.api_v1_pricing_organization_products_change_price_partial_update_archived_reason_error_component import (
            ApiV1PricingOrganizationProductsChangePricePartialUpdateArchivedReasonErrorComponent,
        )
        from ..models.api_v1_pricing_organization_products_change_price_partial_update_auto_managed_error_component import (
            ApiV1PricingOrganizationProductsChangePricePartialUpdateAutoManagedErrorComponent,
        )
        from ..models.api_v1_pricing_organization_products_change_price_partial_update_catalogue_app_error_component import (
            ApiV1PricingOrganizationProductsChangePricePartialUpdateCatalogueAppErrorComponent,
        )
        from ..models.api_v1_pricing_organization_products_change_price_partial_update_content_type_error_component import (
            ApiV1PricingOrganizationProductsChangePricePartialUpdateContentTypeErrorComponent,
        )
        from ..models.api_v1_pricing_organization_products_change_price_partial_update_criticality_error_component import (
            ApiV1PricingOrganizationProductsChangePricePartialUpdateCriticalityErrorComponent,
        )
        from ..models.api_v1_pricing_organization_products_change_price_partial_update_debug_mode_error_component import (
            ApiV1PricingOrganizationProductsChangePricePartialUpdateDebugModeErrorComponent,
        )
        from ..models.api_v1_pricing_organization_products_change_price_partial_update_display_name_error_component import (
            ApiV1PricingOrganizationProductsChangePricePartialUpdateDisplayNameErrorComponent,
        )
        from ..models.api_v1_pricing_organization_products_change_price_partial_update_internal_note_error_component import (
            ApiV1PricingOrganizationProductsChangePricePartialUpdateInternalNoteErrorComponent,
        )
        from ..models.api_v1_pricing_organization_products_change_price_partial_update_kind_error_component import (
            ApiV1PricingOrganizationProductsChangePricePartialUpdateKindErrorComponent,
        )
        from ..models.api_v1_pricing_organization_products_change_price_partial_update_labels_error_component import (
            ApiV1PricingOrganizationProductsChangePricePartialUpdateLabelsErrorComponent,
        )
        from ..models.api_v1_pricing_organization_products_change_price_partial_update_name_error_component import (
            ApiV1PricingOrganizationProductsChangePricePartialUpdateNameErrorComponent,
        )
        from ..models.api_v1_pricing_organization_products_change_price_partial_update_non_field_errors_error_component import (
            ApiV1PricingOrganizationProductsChangePricePartialUpdateNonFieldErrorsErrorComponent,
        )
        from ..models.api_v1_pricing_organization_products_change_price_partial_update_object_id_error_component import (
            ApiV1PricingOrganizationProductsChangePricePartialUpdateObjectIdErrorComponent,
        )
        from ..models.api_v1_pricing_organization_products_change_price_partial_update_platform_service_error_component import (
            ApiV1PricingOrganizationProductsChangePricePartialUpdatePlatformServiceErrorComponent,
        )
        from ..models.api_v1_pricing_organization_products_change_price_partial_update_provider_error_component import (
            ApiV1PricingOrganizationProductsChangePricePartialUpdateProviderErrorComponent,
        )
        from ..models.api_v1_pricing_organization_products_change_price_partial_update_provider_id_error_component import (
            ApiV1PricingOrganizationProductsChangePricePartialUpdateProviderIdErrorComponent,
        )
        from ..models.api_v1_pricing_organization_products_change_price_partial_update_provider_reference_error_component import (
            ApiV1PricingOrganizationProductsChangePricePartialUpdateProviderReferenceErrorComponent,
        )
        from ..models.api_v1_pricing_organization_products_change_price_partial_update_reconciliation_enabled_error_component import (
            ApiV1PricingOrganizationProductsChangePricePartialUpdateReconciliationEnabledErrorComponent,
        )
        from ..models.api_v1_pricing_organization_products_change_price_partial_update_sla_availability_error_component import (
            ApiV1PricingOrganizationProductsChangePricePartialUpdateSlaAvailabilityErrorComponent,
        )
        from ..models.api_v1_pricing_organization_products_change_price_partial_update_sla_target_error_component import (
            ApiV1PricingOrganizationProductsChangePricePartialUpdateSlaTargetErrorComponent,
        )
        from ..models.api_v1_pricing_organization_products_change_price_partial_update_slo_availability_error_component import (
            ApiV1PricingOrganizationProductsChangePricePartialUpdateSloAvailabilityErrorComponent,
        )
        from ..models.api_v1_pricing_organization_products_change_price_partial_update_slo_target_error_component import (
            ApiV1PricingOrganizationProductsChangePricePartialUpdateSloTargetErrorComponent,
        )
        from ..models.api_v1_pricing_organization_products_change_price_partial_update_target_availability_error_component import (
            ApiV1PricingOrganizationProductsChangePricePartialUpdateTargetAvailabilityErrorComponent,
        )
        from ..models.api_v1_pricing_organization_products_change_price_partial_update_tolerations_error_component import (
            ApiV1PricingOrganizationProductsChangePricePartialUpdateTolerationsErrorComponent,
        )

        d = dict(src_dict)
        type_ = check_validation_error_enum(d.pop("type"))

        errors = []
        _errors = d.pop("errors")
        for errors_item_data in _errors:

            def _parse_errors_item(
                data: object,
            ) -> (
                ApiV1PricingOrganizationProductsChangePricePartialUpdateActiveFromErrorComponent
                | ApiV1PricingOrganizationProductsChangePricePartialUpdateActiveUntilErrorComponent
                | ApiV1PricingOrganizationProductsChangePricePartialUpdateAgreedPriceErrorComponent
                | ApiV1PricingOrganizationProductsChangePricePartialUpdateAgreedPriceReasonErrorComponent
                | ApiV1PricingOrganizationProductsChangePricePartialUpdateAnnotationsErrorComponent
                | ApiV1PricingOrganizationProductsChangePricePartialUpdateArchivedAtErrorComponent
                | ApiV1PricingOrganizationProductsChangePricePartialUpdateArchivedErrorComponent
                | ApiV1PricingOrganizationProductsChangePricePartialUpdateArchivedReasonErrorComponent
                | ApiV1PricingOrganizationProductsChangePricePartialUpdateAutoManagedErrorComponent
                | ApiV1PricingOrganizationProductsChangePricePartialUpdateCatalogueAppErrorComponent
                | ApiV1PricingOrganizationProductsChangePricePartialUpdateContentTypeErrorComponent
                | ApiV1PricingOrganizationProductsChangePricePartialUpdateCriticalityErrorComponent
                | ApiV1PricingOrganizationProductsChangePricePartialUpdateDebugModeErrorComponent
                | ApiV1PricingOrganizationProductsChangePricePartialUpdateDisplayNameErrorComponent
                | ApiV1PricingOrganizationProductsChangePricePartialUpdateInternalNoteErrorComponent
                | ApiV1PricingOrganizationProductsChangePricePartialUpdateKindErrorComponent
                | ApiV1PricingOrganizationProductsChangePricePartialUpdateLabelsErrorComponent
                | ApiV1PricingOrganizationProductsChangePricePartialUpdateNameErrorComponent
                | ApiV1PricingOrganizationProductsChangePricePartialUpdateNonFieldErrorsErrorComponent
                | ApiV1PricingOrganizationProductsChangePricePartialUpdateObjectIdErrorComponent
                | ApiV1PricingOrganizationProductsChangePricePartialUpdatePlatformServiceErrorComponent
                | ApiV1PricingOrganizationProductsChangePricePartialUpdateProviderErrorComponent
                | ApiV1PricingOrganizationProductsChangePricePartialUpdateProviderIdErrorComponent
                | ApiV1PricingOrganizationProductsChangePricePartialUpdateProviderReferenceErrorComponent
                | ApiV1PricingOrganizationProductsChangePricePartialUpdateReconciliationEnabledErrorComponent
                | ApiV1PricingOrganizationProductsChangePricePartialUpdateSlaAvailabilityErrorComponent
                | ApiV1PricingOrganizationProductsChangePricePartialUpdateSlaTargetErrorComponent
                | ApiV1PricingOrganizationProductsChangePricePartialUpdateSloAvailabilityErrorComponent
                | ApiV1PricingOrganizationProductsChangePricePartialUpdateSloTargetErrorComponent
                | ApiV1PricingOrganizationProductsChangePricePartialUpdateTargetAvailabilityErrorComponent
                | ApiV1PricingOrganizationProductsChangePricePartialUpdateTolerationsErrorComponent
            ):
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_organization_products_change_price_partial_update_error_type_0 = (
                        ApiV1PricingOrganizationProductsChangePricePartialUpdateNonFieldErrorsErrorComponent.from_dict(
                            data
                        )
                    )

                    return (
                        componentsschemas_api_v1_pricing_organization_products_change_price_partial_update_error_type_0
                    )
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_organization_products_change_price_partial_update_error_type_1 = (
                        ApiV1PricingOrganizationProductsChangePricePartialUpdateNameErrorComponent.from_dict(data)
                    )

                    return (
                        componentsschemas_api_v1_pricing_organization_products_change_price_partial_update_error_type_1
                    )
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_organization_products_change_price_partial_update_error_type_2 = (
                        ApiV1PricingOrganizationProductsChangePricePartialUpdateDisplayNameErrorComponent.from_dict(
                            data
                        )
                    )

                    return (
                        componentsschemas_api_v1_pricing_organization_products_change_price_partial_update_error_type_2
                    )
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_organization_products_change_price_partial_update_error_type_3 = (
                        ApiV1PricingOrganizationProductsChangePricePartialUpdateLabelsErrorComponent.from_dict(data)
                    )

                    return (
                        componentsschemas_api_v1_pricing_organization_products_change_price_partial_update_error_type_3
                    )
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_organization_products_change_price_partial_update_error_type_4 = (
                        ApiV1PricingOrganizationProductsChangePricePartialUpdateAnnotationsErrorComponent.from_dict(
                            data
                        )
                    )

                    return (
                        componentsschemas_api_v1_pricing_organization_products_change_price_partial_update_error_type_4
                    )
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_organization_products_change_price_partial_update_error_type_5 = (
                        ApiV1PricingOrganizationProductsChangePricePartialUpdateDebugModeErrorComponent.from_dict(data)
                    )

                    return (
                        componentsschemas_api_v1_pricing_organization_products_change_price_partial_update_error_type_5
                    )
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_organization_products_change_price_partial_update_error_type_6 = (
                        ApiV1PricingOrganizationProductsChangePricePartialUpdateProviderErrorComponent.from_dict(data)
                    )

                    return (
                        componentsschemas_api_v1_pricing_organization_products_change_price_partial_update_error_type_6
                    )
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_organization_products_change_price_partial_update_error_type_7 = ApiV1PricingOrganizationProductsChangePricePartialUpdateProviderReferenceErrorComponent.from_dict(
                        data
                    )

                    return (
                        componentsschemas_api_v1_pricing_organization_products_change_price_partial_update_error_type_7
                    )
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_organization_products_change_price_partial_update_error_type_8 = (
                        ApiV1PricingOrganizationProductsChangePricePartialUpdateProviderIdErrorComponent.from_dict(data)
                    )

                    return (
                        componentsschemas_api_v1_pricing_organization_products_change_price_partial_update_error_type_8
                    )
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_organization_products_change_price_partial_update_error_type_9 = ApiV1PricingOrganizationProductsChangePricePartialUpdateReconciliationEnabledErrorComponent.from_dict(
                        data
                    )

                    return (
                        componentsschemas_api_v1_pricing_organization_products_change_price_partial_update_error_type_9
                    )
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_organization_products_change_price_partial_update_error_type_10 = (
                        ApiV1PricingOrganizationProductsChangePricePartialUpdatePlatformServiceErrorComponent.from_dict(
                            data
                        )
                    )

                    return (
                        componentsschemas_api_v1_pricing_organization_products_change_price_partial_update_error_type_10
                    )
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_organization_products_change_price_partial_update_error_type_11 = (
                        ApiV1PricingOrganizationProductsChangePricePartialUpdateKindErrorComponent.from_dict(data)
                    )

                    return (
                        componentsschemas_api_v1_pricing_organization_products_change_price_partial_update_error_type_11
                    )
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_organization_products_change_price_partial_update_error_type_12 = (
                        ApiV1PricingOrganizationProductsChangePricePartialUpdateTolerationsErrorComponent.from_dict(
                            data
                        )
                    )

                    return (
                        componentsschemas_api_v1_pricing_organization_products_change_price_partial_update_error_type_12
                    )
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_organization_products_change_price_partial_update_error_type_13 = (
                        ApiV1PricingOrganizationProductsChangePricePartialUpdateArchivedErrorComponent.from_dict(data)
                    )

                    return (
                        componentsschemas_api_v1_pricing_organization_products_change_price_partial_update_error_type_13
                    )
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_organization_products_change_price_partial_update_error_type_14 = (
                        ApiV1PricingOrganizationProductsChangePricePartialUpdateArchivedAtErrorComponent.from_dict(data)
                    )

                    return (
                        componentsschemas_api_v1_pricing_organization_products_change_price_partial_update_error_type_14
                    )
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_organization_products_change_price_partial_update_error_type_15 = (
                        ApiV1PricingOrganizationProductsChangePricePartialUpdateArchivedReasonErrorComponent.from_dict(
                            data
                        )
                    )

                    return (
                        componentsschemas_api_v1_pricing_organization_products_change_price_partial_update_error_type_15
                    )
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_organization_products_change_price_partial_update_error_type_16 = (
                        ApiV1PricingOrganizationProductsChangePricePartialUpdateCriticalityErrorComponent.from_dict(
                            data
                        )
                    )

                    return (
                        componentsschemas_api_v1_pricing_organization_products_change_price_partial_update_error_type_16
                    )
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_organization_products_change_price_partial_update_error_type_17 = ApiV1PricingOrganizationProductsChangePricePartialUpdateTargetAvailabilityErrorComponent.from_dict(
                        data
                    )

                    return (
                        componentsschemas_api_v1_pricing_organization_products_change_price_partial_update_error_type_17
                    )
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_organization_products_change_price_partial_update_error_type_18 = (
                        ApiV1PricingOrganizationProductsChangePricePartialUpdateSloTargetErrorComponent.from_dict(data)
                    )

                    return (
                        componentsschemas_api_v1_pricing_organization_products_change_price_partial_update_error_type_18
                    )
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_organization_products_change_price_partial_update_error_type_19 = (
                        ApiV1PricingOrganizationProductsChangePricePartialUpdateSloAvailabilityErrorComponent.from_dict(
                            data
                        )
                    )

                    return (
                        componentsschemas_api_v1_pricing_organization_products_change_price_partial_update_error_type_19
                    )
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_organization_products_change_price_partial_update_error_type_20 = (
                        ApiV1PricingOrganizationProductsChangePricePartialUpdateSlaTargetErrorComponent.from_dict(data)
                    )

                    return (
                        componentsschemas_api_v1_pricing_organization_products_change_price_partial_update_error_type_20
                    )
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_organization_products_change_price_partial_update_error_type_21 = (
                        ApiV1PricingOrganizationProductsChangePricePartialUpdateSlaAvailabilityErrorComponent.from_dict(
                            data
                        )
                    )

                    return (
                        componentsschemas_api_v1_pricing_organization_products_change_price_partial_update_error_type_21
                    )
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_organization_products_change_price_partial_update_error_type_22 = (
                        ApiV1PricingOrganizationProductsChangePricePartialUpdateCatalogueAppErrorComponent.from_dict(
                            data
                        )
                    )

                    return (
                        componentsschemas_api_v1_pricing_organization_products_change_price_partial_update_error_type_22
                    )
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_organization_products_change_price_partial_update_error_type_23 = (
                        ApiV1PricingOrganizationProductsChangePricePartialUpdateContentTypeErrorComponent.from_dict(
                            data
                        )
                    )

                    return (
                        componentsschemas_api_v1_pricing_organization_products_change_price_partial_update_error_type_23
                    )
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_organization_products_change_price_partial_update_error_type_24 = (
                        ApiV1PricingOrganizationProductsChangePricePartialUpdateObjectIdErrorComponent.from_dict(data)
                    )

                    return (
                        componentsschemas_api_v1_pricing_organization_products_change_price_partial_update_error_type_24
                    )
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_organization_products_change_price_partial_update_error_type_25 = (
                        ApiV1PricingOrganizationProductsChangePricePartialUpdateAutoManagedErrorComponent.from_dict(
                            data
                        )
                    )

                    return (
                        componentsschemas_api_v1_pricing_organization_products_change_price_partial_update_error_type_25
                    )
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_organization_products_change_price_partial_update_error_type_26 = (
                        ApiV1PricingOrganizationProductsChangePricePartialUpdateActiveFromErrorComponent.from_dict(data)
                    )

                    return (
                        componentsschemas_api_v1_pricing_organization_products_change_price_partial_update_error_type_26
                    )
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_organization_products_change_price_partial_update_error_type_27 = (
                        ApiV1PricingOrganizationProductsChangePricePartialUpdateActiveUntilErrorComponent.from_dict(
                            data
                        )
                    )

                    return (
                        componentsschemas_api_v1_pricing_organization_products_change_price_partial_update_error_type_27
                    )
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_organization_products_change_price_partial_update_error_type_28 = (
                        ApiV1PricingOrganizationProductsChangePricePartialUpdateAgreedPriceErrorComponent.from_dict(
                            data
                        )
                    )

                    return (
                        componentsschemas_api_v1_pricing_organization_products_change_price_partial_update_error_type_28
                    )
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_organization_products_change_price_partial_update_error_type_29 = ApiV1PricingOrganizationProductsChangePricePartialUpdateAgreedPriceReasonErrorComponent.from_dict(
                        data
                    )

                    return (
                        componentsschemas_api_v1_pricing_organization_products_change_price_partial_update_error_type_29
                    )
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_api_v1_pricing_organization_products_change_price_partial_update_error_type_30 = (
                    ApiV1PricingOrganizationProductsChangePricePartialUpdateInternalNoteErrorComponent.from_dict(data)
                )

                return componentsschemas_api_v1_pricing_organization_products_change_price_partial_update_error_type_30

            errors_item = _parse_errors_item(errors_item_data)

            errors.append(errors_item)

        api_v1_pricing_organization_products_change_price_partial_update_validation_error = cls(
            type_=type_,
            errors=errors,
        )

        api_v1_pricing_organization_products_change_price_partial_update_validation_error.additional_properties = d
        return api_v1_pricing_organization_products_change_price_partial_update_validation_error

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
