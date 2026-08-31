from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.validation_error_enum import ValidationErrorEnum, check_validation_error_enum

if TYPE_CHECKING:
    from ..models.api_v1_pricing_organization_products_partial_update_active_from_error_component import (
        ApiV1PricingOrganizationProductsPartialUpdateActiveFromErrorComponent,
    )
    from ..models.api_v1_pricing_organization_products_partial_update_active_until_error_component import (
        ApiV1PricingOrganizationProductsPartialUpdateActiveUntilErrorComponent,
    )
    from ..models.api_v1_pricing_organization_products_partial_update_agreed_price_error_component import (
        ApiV1PricingOrganizationProductsPartialUpdateAgreedPriceErrorComponent,
    )
    from ..models.api_v1_pricing_organization_products_partial_update_agreed_price_reason_error_component import (
        ApiV1PricingOrganizationProductsPartialUpdateAgreedPriceReasonErrorComponent,
    )
    from ..models.api_v1_pricing_organization_products_partial_update_annotations_error_component import (
        ApiV1PricingOrganizationProductsPartialUpdateAnnotationsErrorComponent,
    )
    from ..models.api_v1_pricing_organization_products_partial_update_archived_at_error_component import (
        ApiV1PricingOrganizationProductsPartialUpdateArchivedAtErrorComponent,
    )
    from ..models.api_v1_pricing_organization_products_partial_update_archived_error_component import (
        ApiV1PricingOrganizationProductsPartialUpdateArchivedErrorComponent,
    )
    from ..models.api_v1_pricing_organization_products_partial_update_archived_reason_error_component import (
        ApiV1PricingOrganizationProductsPartialUpdateArchivedReasonErrorComponent,
    )
    from ..models.api_v1_pricing_organization_products_partial_update_auto_managed_error_component import (
        ApiV1PricingOrganizationProductsPartialUpdateAutoManagedErrorComponent,
    )
    from ..models.api_v1_pricing_organization_products_partial_update_catalogue_app_error_component import (
        ApiV1PricingOrganizationProductsPartialUpdateCatalogueAppErrorComponent,
    )
    from ..models.api_v1_pricing_organization_products_partial_update_content_type_error_component import (
        ApiV1PricingOrganizationProductsPartialUpdateContentTypeErrorComponent,
    )
    from ..models.api_v1_pricing_organization_products_partial_update_criticality_error_component import (
        ApiV1PricingOrganizationProductsPartialUpdateCriticalityErrorComponent,
    )
    from ..models.api_v1_pricing_organization_products_partial_update_debug_mode_error_component import (
        ApiV1PricingOrganizationProductsPartialUpdateDebugModeErrorComponent,
    )
    from ..models.api_v1_pricing_organization_products_partial_update_display_name_error_component import (
        ApiV1PricingOrganizationProductsPartialUpdateDisplayNameErrorComponent,
    )
    from ..models.api_v1_pricing_organization_products_partial_update_internal_note_error_component import (
        ApiV1PricingOrganizationProductsPartialUpdateInternalNoteErrorComponent,
    )
    from ..models.api_v1_pricing_organization_products_partial_update_kind_error_component import (
        ApiV1PricingOrganizationProductsPartialUpdateKindErrorComponent,
    )
    from ..models.api_v1_pricing_organization_products_partial_update_labels_error_component import (
        ApiV1PricingOrganizationProductsPartialUpdateLabelsErrorComponent,
    )
    from ..models.api_v1_pricing_organization_products_partial_update_name_error_component import (
        ApiV1PricingOrganizationProductsPartialUpdateNameErrorComponent,
    )
    from ..models.api_v1_pricing_organization_products_partial_update_non_field_errors_error_component import (
        ApiV1PricingOrganizationProductsPartialUpdateNonFieldErrorsErrorComponent,
    )
    from ..models.api_v1_pricing_organization_products_partial_update_object_id_error_component import (
        ApiV1PricingOrganizationProductsPartialUpdateObjectIdErrorComponent,
    )
    from ..models.api_v1_pricing_organization_products_partial_update_platform_service_error_component import (
        ApiV1PricingOrganizationProductsPartialUpdatePlatformServiceErrorComponent,
    )
    from ..models.api_v1_pricing_organization_products_partial_update_provider_error_component import (
        ApiV1PricingOrganizationProductsPartialUpdateProviderErrorComponent,
    )
    from ..models.api_v1_pricing_organization_products_partial_update_provider_id_error_component import (
        ApiV1PricingOrganizationProductsPartialUpdateProviderIdErrorComponent,
    )
    from ..models.api_v1_pricing_organization_products_partial_update_provider_reference_error_component import (
        ApiV1PricingOrganizationProductsPartialUpdateProviderReferenceErrorComponent,
    )
    from ..models.api_v1_pricing_organization_products_partial_update_reconciliation_enabled_error_component import (
        ApiV1PricingOrganizationProductsPartialUpdateReconciliationEnabledErrorComponent,
    )
    from ..models.api_v1_pricing_organization_products_partial_update_sla_availability_error_component import (
        ApiV1PricingOrganizationProductsPartialUpdateSlaAvailabilityErrorComponent,
    )
    from ..models.api_v1_pricing_organization_products_partial_update_sla_target_error_component import (
        ApiV1PricingOrganizationProductsPartialUpdateSlaTargetErrorComponent,
    )
    from ..models.api_v1_pricing_organization_products_partial_update_slo_availability_error_component import (
        ApiV1PricingOrganizationProductsPartialUpdateSloAvailabilityErrorComponent,
    )
    from ..models.api_v1_pricing_organization_products_partial_update_slo_target_error_component import (
        ApiV1PricingOrganizationProductsPartialUpdateSloTargetErrorComponent,
    )
    from ..models.api_v1_pricing_organization_products_partial_update_target_availability_error_component import (
        ApiV1PricingOrganizationProductsPartialUpdateTargetAvailabilityErrorComponent,
    )
    from ..models.api_v1_pricing_organization_products_partial_update_tolerations_error_component import (
        ApiV1PricingOrganizationProductsPartialUpdateTolerationsErrorComponent,
    )


T = TypeVar("T", bound="ApiV1PricingOrganizationProductsPartialUpdateValidationError")


@_attrs_define
class ApiV1PricingOrganizationProductsPartialUpdateValidationError:
    """
    Attributes:
        type_ (ValidationErrorEnum): * `validation_error` - Validation Error
        errors (list[ApiV1PricingOrganizationProductsPartialUpdateActiveFromErrorComponent |
            ApiV1PricingOrganizationProductsPartialUpdateActiveUntilErrorComponent |
            ApiV1PricingOrganizationProductsPartialUpdateAgreedPriceErrorComponent |
            ApiV1PricingOrganizationProductsPartialUpdateAgreedPriceReasonErrorComponent |
            ApiV1PricingOrganizationProductsPartialUpdateAnnotationsErrorComponent |
            ApiV1PricingOrganizationProductsPartialUpdateArchivedAtErrorComponent |
            ApiV1PricingOrganizationProductsPartialUpdateArchivedErrorComponent |
            ApiV1PricingOrganizationProductsPartialUpdateArchivedReasonErrorComponent |
            ApiV1PricingOrganizationProductsPartialUpdateAutoManagedErrorComponent |
            ApiV1PricingOrganizationProductsPartialUpdateCatalogueAppErrorComponent |
            ApiV1PricingOrganizationProductsPartialUpdateContentTypeErrorComponent |
            ApiV1PricingOrganizationProductsPartialUpdateCriticalityErrorComponent |
            ApiV1PricingOrganizationProductsPartialUpdateDebugModeErrorComponent |
            ApiV1PricingOrganizationProductsPartialUpdateDisplayNameErrorComponent |
            ApiV1PricingOrganizationProductsPartialUpdateInternalNoteErrorComponent |
            ApiV1PricingOrganizationProductsPartialUpdateKindErrorComponent |
            ApiV1PricingOrganizationProductsPartialUpdateLabelsErrorComponent |
            ApiV1PricingOrganizationProductsPartialUpdateNameErrorComponent |
            ApiV1PricingOrganizationProductsPartialUpdateNonFieldErrorsErrorComponent |
            ApiV1PricingOrganizationProductsPartialUpdateObjectIdErrorComponent |
            ApiV1PricingOrganizationProductsPartialUpdatePlatformServiceErrorComponent |
            ApiV1PricingOrganizationProductsPartialUpdateProviderErrorComponent |
            ApiV1PricingOrganizationProductsPartialUpdateProviderIdErrorComponent |
            ApiV1PricingOrganizationProductsPartialUpdateProviderReferenceErrorComponent |
            ApiV1PricingOrganizationProductsPartialUpdateReconciliationEnabledErrorComponent |
            ApiV1PricingOrganizationProductsPartialUpdateSlaAvailabilityErrorComponent |
            ApiV1PricingOrganizationProductsPartialUpdateSlaTargetErrorComponent |
            ApiV1PricingOrganizationProductsPartialUpdateSloAvailabilityErrorComponent |
            ApiV1PricingOrganizationProductsPartialUpdateSloTargetErrorComponent |
            ApiV1PricingOrganizationProductsPartialUpdateTargetAvailabilityErrorComponent |
            ApiV1PricingOrganizationProductsPartialUpdateTolerationsErrorComponent]):
    """

    type_: ValidationErrorEnum
    errors: list[
        ApiV1PricingOrganizationProductsPartialUpdateActiveFromErrorComponent
        | ApiV1PricingOrganizationProductsPartialUpdateActiveUntilErrorComponent
        | ApiV1PricingOrganizationProductsPartialUpdateAgreedPriceErrorComponent
        | ApiV1PricingOrganizationProductsPartialUpdateAgreedPriceReasonErrorComponent
        | ApiV1PricingOrganizationProductsPartialUpdateAnnotationsErrorComponent
        | ApiV1PricingOrganizationProductsPartialUpdateArchivedAtErrorComponent
        | ApiV1PricingOrganizationProductsPartialUpdateArchivedErrorComponent
        | ApiV1PricingOrganizationProductsPartialUpdateArchivedReasonErrorComponent
        | ApiV1PricingOrganizationProductsPartialUpdateAutoManagedErrorComponent
        | ApiV1PricingOrganizationProductsPartialUpdateCatalogueAppErrorComponent
        | ApiV1PricingOrganizationProductsPartialUpdateContentTypeErrorComponent
        | ApiV1PricingOrganizationProductsPartialUpdateCriticalityErrorComponent
        | ApiV1PricingOrganizationProductsPartialUpdateDebugModeErrorComponent
        | ApiV1PricingOrganizationProductsPartialUpdateDisplayNameErrorComponent
        | ApiV1PricingOrganizationProductsPartialUpdateInternalNoteErrorComponent
        | ApiV1PricingOrganizationProductsPartialUpdateKindErrorComponent
        | ApiV1PricingOrganizationProductsPartialUpdateLabelsErrorComponent
        | ApiV1PricingOrganizationProductsPartialUpdateNameErrorComponent
        | ApiV1PricingOrganizationProductsPartialUpdateNonFieldErrorsErrorComponent
        | ApiV1PricingOrganizationProductsPartialUpdateObjectIdErrorComponent
        | ApiV1PricingOrganizationProductsPartialUpdatePlatformServiceErrorComponent
        | ApiV1PricingOrganizationProductsPartialUpdateProviderErrorComponent
        | ApiV1PricingOrganizationProductsPartialUpdateProviderIdErrorComponent
        | ApiV1PricingOrganizationProductsPartialUpdateProviderReferenceErrorComponent
        | ApiV1PricingOrganizationProductsPartialUpdateReconciliationEnabledErrorComponent
        | ApiV1PricingOrganizationProductsPartialUpdateSlaAvailabilityErrorComponent
        | ApiV1PricingOrganizationProductsPartialUpdateSlaTargetErrorComponent
        | ApiV1PricingOrganizationProductsPartialUpdateSloAvailabilityErrorComponent
        | ApiV1PricingOrganizationProductsPartialUpdateSloTargetErrorComponent
        | ApiV1PricingOrganizationProductsPartialUpdateTargetAvailabilityErrorComponent
        | ApiV1PricingOrganizationProductsPartialUpdateTolerationsErrorComponent
    ]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.api_v1_pricing_organization_products_partial_update_active_from_error_component import (
            ApiV1PricingOrganizationProductsPartialUpdateActiveFromErrorComponent,
        )
        from ..models.api_v1_pricing_organization_products_partial_update_active_until_error_component import (
            ApiV1PricingOrganizationProductsPartialUpdateActiveUntilErrorComponent,
        )
        from ..models.api_v1_pricing_organization_products_partial_update_agreed_price_error_component import (
            ApiV1PricingOrganizationProductsPartialUpdateAgreedPriceErrorComponent,
        )
        from ..models.api_v1_pricing_organization_products_partial_update_agreed_price_reason_error_component import (
            ApiV1PricingOrganizationProductsPartialUpdateAgreedPriceReasonErrorComponent,
        )
        from ..models.api_v1_pricing_organization_products_partial_update_annotations_error_component import (
            ApiV1PricingOrganizationProductsPartialUpdateAnnotationsErrorComponent,
        )
        from ..models.api_v1_pricing_organization_products_partial_update_archived_at_error_component import (
            ApiV1PricingOrganizationProductsPartialUpdateArchivedAtErrorComponent,
        )
        from ..models.api_v1_pricing_organization_products_partial_update_archived_error_component import (
            ApiV1PricingOrganizationProductsPartialUpdateArchivedErrorComponent,
        )
        from ..models.api_v1_pricing_organization_products_partial_update_archived_reason_error_component import (
            ApiV1PricingOrganizationProductsPartialUpdateArchivedReasonErrorComponent,
        )
        from ..models.api_v1_pricing_organization_products_partial_update_auto_managed_error_component import (
            ApiV1PricingOrganizationProductsPartialUpdateAutoManagedErrorComponent,
        )
        from ..models.api_v1_pricing_organization_products_partial_update_catalogue_app_error_component import (
            ApiV1PricingOrganizationProductsPartialUpdateCatalogueAppErrorComponent,
        )
        from ..models.api_v1_pricing_organization_products_partial_update_content_type_error_component import (
            ApiV1PricingOrganizationProductsPartialUpdateContentTypeErrorComponent,
        )
        from ..models.api_v1_pricing_organization_products_partial_update_criticality_error_component import (
            ApiV1PricingOrganizationProductsPartialUpdateCriticalityErrorComponent,
        )
        from ..models.api_v1_pricing_organization_products_partial_update_debug_mode_error_component import (
            ApiV1PricingOrganizationProductsPartialUpdateDebugModeErrorComponent,
        )
        from ..models.api_v1_pricing_organization_products_partial_update_display_name_error_component import (
            ApiV1PricingOrganizationProductsPartialUpdateDisplayNameErrorComponent,
        )
        from ..models.api_v1_pricing_organization_products_partial_update_kind_error_component import (
            ApiV1PricingOrganizationProductsPartialUpdateKindErrorComponent,
        )
        from ..models.api_v1_pricing_organization_products_partial_update_labels_error_component import (
            ApiV1PricingOrganizationProductsPartialUpdateLabelsErrorComponent,
        )
        from ..models.api_v1_pricing_organization_products_partial_update_name_error_component import (
            ApiV1PricingOrganizationProductsPartialUpdateNameErrorComponent,
        )
        from ..models.api_v1_pricing_organization_products_partial_update_non_field_errors_error_component import (
            ApiV1PricingOrganizationProductsPartialUpdateNonFieldErrorsErrorComponent,
        )
        from ..models.api_v1_pricing_organization_products_partial_update_object_id_error_component import (
            ApiV1PricingOrganizationProductsPartialUpdateObjectIdErrorComponent,
        )
        from ..models.api_v1_pricing_organization_products_partial_update_platform_service_error_component import (
            ApiV1PricingOrganizationProductsPartialUpdatePlatformServiceErrorComponent,
        )
        from ..models.api_v1_pricing_organization_products_partial_update_provider_error_component import (
            ApiV1PricingOrganizationProductsPartialUpdateProviderErrorComponent,
        )
        from ..models.api_v1_pricing_organization_products_partial_update_provider_id_error_component import (
            ApiV1PricingOrganizationProductsPartialUpdateProviderIdErrorComponent,
        )
        from ..models.api_v1_pricing_organization_products_partial_update_provider_reference_error_component import (
            ApiV1PricingOrganizationProductsPartialUpdateProviderReferenceErrorComponent,
        )
        from ..models.api_v1_pricing_organization_products_partial_update_reconciliation_enabled_error_component import (
            ApiV1PricingOrganizationProductsPartialUpdateReconciliationEnabledErrorComponent,
        )
        from ..models.api_v1_pricing_organization_products_partial_update_sla_availability_error_component import (
            ApiV1PricingOrganizationProductsPartialUpdateSlaAvailabilityErrorComponent,
        )
        from ..models.api_v1_pricing_organization_products_partial_update_sla_target_error_component import (
            ApiV1PricingOrganizationProductsPartialUpdateSlaTargetErrorComponent,
        )
        from ..models.api_v1_pricing_organization_products_partial_update_slo_availability_error_component import (
            ApiV1PricingOrganizationProductsPartialUpdateSloAvailabilityErrorComponent,
        )
        from ..models.api_v1_pricing_organization_products_partial_update_slo_target_error_component import (
            ApiV1PricingOrganizationProductsPartialUpdateSloTargetErrorComponent,
        )
        from ..models.api_v1_pricing_organization_products_partial_update_target_availability_error_component import (
            ApiV1PricingOrganizationProductsPartialUpdateTargetAvailabilityErrorComponent,
        )
        from ..models.api_v1_pricing_organization_products_partial_update_tolerations_error_component import (
            ApiV1PricingOrganizationProductsPartialUpdateTolerationsErrorComponent,
        )

        type_: str = self.type_

        errors = []
        for errors_item_data in self.errors:
            errors_item: dict[str, Any]
            if isinstance(errors_item_data, ApiV1PricingOrganizationProductsPartialUpdateNonFieldErrorsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingOrganizationProductsPartialUpdateNameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingOrganizationProductsPartialUpdateDisplayNameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingOrganizationProductsPartialUpdateLabelsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingOrganizationProductsPartialUpdateAnnotationsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingOrganizationProductsPartialUpdateDebugModeErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingOrganizationProductsPartialUpdateProviderErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(
                errors_item_data, ApiV1PricingOrganizationProductsPartialUpdateProviderReferenceErrorComponent
            ):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingOrganizationProductsPartialUpdateProviderIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(
                errors_item_data, ApiV1PricingOrganizationProductsPartialUpdateReconciliationEnabledErrorComponent
            ):
                errors_item = errors_item_data.to_dict()
            elif isinstance(
                errors_item_data, ApiV1PricingOrganizationProductsPartialUpdatePlatformServiceErrorComponent
            ):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingOrganizationProductsPartialUpdateKindErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingOrganizationProductsPartialUpdateTolerationsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingOrganizationProductsPartialUpdateArchivedErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingOrganizationProductsPartialUpdateArchivedAtErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(
                errors_item_data, ApiV1PricingOrganizationProductsPartialUpdateArchivedReasonErrorComponent
            ):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingOrganizationProductsPartialUpdateCriticalityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(
                errors_item_data, ApiV1PricingOrganizationProductsPartialUpdateTargetAvailabilityErrorComponent
            ):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingOrganizationProductsPartialUpdateSloTargetErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(
                errors_item_data, ApiV1PricingOrganizationProductsPartialUpdateSloAvailabilityErrorComponent
            ):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingOrganizationProductsPartialUpdateSlaTargetErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(
                errors_item_data, ApiV1PricingOrganizationProductsPartialUpdateSlaAvailabilityErrorComponent
            ):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingOrganizationProductsPartialUpdateCatalogueAppErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingOrganizationProductsPartialUpdateContentTypeErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingOrganizationProductsPartialUpdateObjectIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingOrganizationProductsPartialUpdateAutoManagedErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingOrganizationProductsPartialUpdateActiveFromErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingOrganizationProductsPartialUpdateActiveUntilErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingOrganizationProductsPartialUpdateAgreedPriceErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(
                errors_item_data, ApiV1PricingOrganizationProductsPartialUpdateAgreedPriceReasonErrorComponent
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
        from ..models.api_v1_pricing_organization_products_partial_update_active_from_error_component import (
            ApiV1PricingOrganizationProductsPartialUpdateActiveFromErrorComponent,
        )
        from ..models.api_v1_pricing_organization_products_partial_update_active_until_error_component import (
            ApiV1PricingOrganizationProductsPartialUpdateActiveUntilErrorComponent,
        )
        from ..models.api_v1_pricing_organization_products_partial_update_agreed_price_error_component import (
            ApiV1PricingOrganizationProductsPartialUpdateAgreedPriceErrorComponent,
        )
        from ..models.api_v1_pricing_organization_products_partial_update_agreed_price_reason_error_component import (
            ApiV1PricingOrganizationProductsPartialUpdateAgreedPriceReasonErrorComponent,
        )
        from ..models.api_v1_pricing_organization_products_partial_update_annotations_error_component import (
            ApiV1PricingOrganizationProductsPartialUpdateAnnotationsErrorComponent,
        )
        from ..models.api_v1_pricing_organization_products_partial_update_archived_at_error_component import (
            ApiV1PricingOrganizationProductsPartialUpdateArchivedAtErrorComponent,
        )
        from ..models.api_v1_pricing_organization_products_partial_update_archived_error_component import (
            ApiV1PricingOrganizationProductsPartialUpdateArchivedErrorComponent,
        )
        from ..models.api_v1_pricing_organization_products_partial_update_archived_reason_error_component import (
            ApiV1PricingOrganizationProductsPartialUpdateArchivedReasonErrorComponent,
        )
        from ..models.api_v1_pricing_organization_products_partial_update_auto_managed_error_component import (
            ApiV1PricingOrganizationProductsPartialUpdateAutoManagedErrorComponent,
        )
        from ..models.api_v1_pricing_organization_products_partial_update_catalogue_app_error_component import (
            ApiV1PricingOrganizationProductsPartialUpdateCatalogueAppErrorComponent,
        )
        from ..models.api_v1_pricing_organization_products_partial_update_content_type_error_component import (
            ApiV1PricingOrganizationProductsPartialUpdateContentTypeErrorComponent,
        )
        from ..models.api_v1_pricing_organization_products_partial_update_criticality_error_component import (
            ApiV1PricingOrganizationProductsPartialUpdateCriticalityErrorComponent,
        )
        from ..models.api_v1_pricing_organization_products_partial_update_debug_mode_error_component import (
            ApiV1PricingOrganizationProductsPartialUpdateDebugModeErrorComponent,
        )
        from ..models.api_v1_pricing_organization_products_partial_update_display_name_error_component import (
            ApiV1PricingOrganizationProductsPartialUpdateDisplayNameErrorComponent,
        )
        from ..models.api_v1_pricing_organization_products_partial_update_internal_note_error_component import (
            ApiV1PricingOrganizationProductsPartialUpdateInternalNoteErrorComponent,
        )
        from ..models.api_v1_pricing_organization_products_partial_update_kind_error_component import (
            ApiV1PricingOrganizationProductsPartialUpdateKindErrorComponent,
        )
        from ..models.api_v1_pricing_organization_products_partial_update_labels_error_component import (
            ApiV1PricingOrganizationProductsPartialUpdateLabelsErrorComponent,
        )
        from ..models.api_v1_pricing_organization_products_partial_update_name_error_component import (
            ApiV1PricingOrganizationProductsPartialUpdateNameErrorComponent,
        )
        from ..models.api_v1_pricing_organization_products_partial_update_non_field_errors_error_component import (
            ApiV1PricingOrganizationProductsPartialUpdateNonFieldErrorsErrorComponent,
        )
        from ..models.api_v1_pricing_organization_products_partial_update_object_id_error_component import (
            ApiV1PricingOrganizationProductsPartialUpdateObjectIdErrorComponent,
        )
        from ..models.api_v1_pricing_organization_products_partial_update_platform_service_error_component import (
            ApiV1PricingOrganizationProductsPartialUpdatePlatformServiceErrorComponent,
        )
        from ..models.api_v1_pricing_organization_products_partial_update_provider_error_component import (
            ApiV1PricingOrganizationProductsPartialUpdateProviderErrorComponent,
        )
        from ..models.api_v1_pricing_organization_products_partial_update_provider_id_error_component import (
            ApiV1PricingOrganizationProductsPartialUpdateProviderIdErrorComponent,
        )
        from ..models.api_v1_pricing_organization_products_partial_update_provider_reference_error_component import (
            ApiV1PricingOrganizationProductsPartialUpdateProviderReferenceErrorComponent,
        )
        from ..models.api_v1_pricing_organization_products_partial_update_reconciliation_enabled_error_component import (
            ApiV1PricingOrganizationProductsPartialUpdateReconciliationEnabledErrorComponent,
        )
        from ..models.api_v1_pricing_organization_products_partial_update_sla_availability_error_component import (
            ApiV1PricingOrganizationProductsPartialUpdateSlaAvailabilityErrorComponent,
        )
        from ..models.api_v1_pricing_organization_products_partial_update_sla_target_error_component import (
            ApiV1PricingOrganizationProductsPartialUpdateSlaTargetErrorComponent,
        )
        from ..models.api_v1_pricing_organization_products_partial_update_slo_availability_error_component import (
            ApiV1PricingOrganizationProductsPartialUpdateSloAvailabilityErrorComponent,
        )
        from ..models.api_v1_pricing_organization_products_partial_update_slo_target_error_component import (
            ApiV1PricingOrganizationProductsPartialUpdateSloTargetErrorComponent,
        )
        from ..models.api_v1_pricing_organization_products_partial_update_target_availability_error_component import (
            ApiV1PricingOrganizationProductsPartialUpdateTargetAvailabilityErrorComponent,
        )
        from ..models.api_v1_pricing_organization_products_partial_update_tolerations_error_component import (
            ApiV1PricingOrganizationProductsPartialUpdateTolerationsErrorComponent,
        )

        d = dict(src_dict)
        type_ = check_validation_error_enum(d.pop("type"))

        errors = []
        _errors = d.pop("errors")
        for errors_item_data in _errors:

            def _parse_errors_item(
                data: object,
            ) -> (
                ApiV1PricingOrganizationProductsPartialUpdateActiveFromErrorComponent
                | ApiV1PricingOrganizationProductsPartialUpdateActiveUntilErrorComponent
                | ApiV1PricingOrganizationProductsPartialUpdateAgreedPriceErrorComponent
                | ApiV1PricingOrganizationProductsPartialUpdateAgreedPriceReasonErrorComponent
                | ApiV1PricingOrganizationProductsPartialUpdateAnnotationsErrorComponent
                | ApiV1PricingOrganizationProductsPartialUpdateArchivedAtErrorComponent
                | ApiV1PricingOrganizationProductsPartialUpdateArchivedErrorComponent
                | ApiV1PricingOrganizationProductsPartialUpdateArchivedReasonErrorComponent
                | ApiV1PricingOrganizationProductsPartialUpdateAutoManagedErrorComponent
                | ApiV1PricingOrganizationProductsPartialUpdateCatalogueAppErrorComponent
                | ApiV1PricingOrganizationProductsPartialUpdateContentTypeErrorComponent
                | ApiV1PricingOrganizationProductsPartialUpdateCriticalityErrorComponent
                | ApiV1PricingOrganizationProductsPartialUpdateDebugModeErrorComponent
                | ApiV1PricingOrganizationProductsPartialUpdateDisplayNameErrorComponent
                | ApiV1PricingOrganizationProductsPartialUpdateInternalNoteErrorComponent
                | ApiV1PricingOrganizationProductsPartialUpdateKindErrorComponent
                | ApiV1PricingOrganizationProductsPartialUpdateLabelsErrorComponent
                | ApiV1PricingOrganizationProductsPartialUpdateNameErrorComponent
                | ApiV1PricingOrganizationProductsPartialUpdateNonFieldErrorsErrorComponent
                | ApiV1PricingOrganizationProductsPartialUpdateObjectIdErrorComponent
                | ApiV1PricingOrganizationProductsPartialUpdatePlatformServiceErrorComponent
                | ApiV1PricingOrganizationProductsPartialUpdateProviderErrorComponent
                | ApiV1PricingOrganizationProductsPartialUpdateProviderIdErrorComponent
                | ApiV1PricingOrganizationProductsPartialUpdateProviderReferenceErrorComponent
                | ApiV1PricingOrganizationProductsPartialUpdateReconciliationEnabledErrorComponent
                | ApiV1PricingOrganizationProductsPartialUpdateSlaAvailabilityErrorComponent
                | ApiV1PricingOrganizationProductsPartialUpdateSlaTargetErrorComponent
                | ApiV1PricingOrganizationProductsPartialUpdateSloAvailabilityErrorComponent
                | ApiV1PricingOrganizationProductsPartialUpdateSloTargetErrorComponent
                | ApiV1PricingOrganizationProductsPartialUpdateTargetAvailabilityErrorComponent
                | ApiV1PricingOrganizationProductsPartialUpdateTolerationsErrorComponent
            ):
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_organization_products_partial_update_error_type_0 = (
                        ApiV1PricingOrganizationProductsPartialUpdateNonFieldErrorsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_organization_products_partial_update_error_type_0
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_organization_products_partial_update_error_type_1 = (
                        ApiV1PricingOrganizationProductsPartialUpdateNameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_organization_products_partial_update_error_type_1
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_organization_products_partial_update_error_type_2 = (
                        ApiV1PricingOrganizationProductsPartialUpdateDisplayNameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_organization_products_partial_update_error_type_2
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_organization_products_partial_update_error_type_3 = (
                        ApiV1PricingOrganizationProductsPartialUpdateLabelsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_organization_products_partial_update_error_type_3
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_organization_products_partial_update_error_type_4 = (
                        ApiV1PricingOrganizationProductsPartialUpdateAnnotationsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_organization_products_partial_update_error_type_4
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_organization_products_partial_update_error_type_5 = (
                        ApiV1PricingOrganizationProductsPartialUpdateDebugModeErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_organization_products_partial_update_error_type_5
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_organization_products_partial_update_error_type_6 = (
                        ApiV1PricingOrganizationProductsPartialUpdateProviderErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_organization_products_partial_update_error_type_6
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_organization_products_partial_update_error_type_7 = (
                        ApiV1PricingOrganizationProductsPartialUpdateProviderReferenceErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_organization_products_partial_update_error_type_7
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_organization_products_partial_update_error_type_8 = (
                        ApiV1PricingOrganizationProductsPartialUpdateProviderIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_organization_products_partial_update_error_type_8
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_organization_products_partial_update_error_type_9 = (
                        ApiV1PricingOrganizationProductsPartialUpdateReconciliationEnabledErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_organization_products_partial_update_error_type_9
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_organization_products_partial_update_error_type_10 = (
                        ApiV1PricingOrganizationProductsPartialUpdatePlatformServiceErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_organization_products_partial_update_error_type_10
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_organization_products_partial_update_error_type_11 = (
                        ApiV1PricingOrganizationProductsPartialUpdateKindErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_organization_products_partial_update_error_type_11
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_organization_products_partial_update_error_type_12 = (
                        ApiV1PricingOrganizationProductsPartialUpdateTolerationsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_organization_products_partial_update_error_type_12
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_organization_products_partial_update_error_type_13 = (
                        ApiV1PricingOrganizationProductsPartialUpdateArchivedErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_organization_products_partial_update_error_type_13
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_organization_products_partial_update_error_type_14 = (
                        ApiV1PricingOrganizationProductsPartialUpdateArchivedAtErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_organization_products_partial_update_error_type_14
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_organization_products_partial_update_error_type_15 = (
                        ApiV1PricingOrganizationProductsPartialUpdateArchivedReasonErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_organization_products_partial_update_error_type_15
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_organization_products_partial_update_error_type_16 = (
                        ApiV1PricingOrganizationProductsPartialUpdateCriticalityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_organization_products_partial_update_error_type_16
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_organization_products_partial_update_error_type_17 = (
                        ApiV1PricingOrganizationProductsPartialUpdateTargetAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_organization_products_partial_update_error_type_17
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_organization_products_partial_update_error_type_18 = (
                        ApiV1PricingOrganizationProductsPartialUpdateSloTargetErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_organization_products_partial_update_error_type_18
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_organization_products_partial_update_error_type_19 = (
                        ApiV1PricingOrganizationProductsPartialUpdateSloAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_organization_products_partial_update_error_type_19
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_organization_products_partial_update_error_type_20 = (
                        ApiV1PricingOrganizationProductsPartialUpdateSlaTargetErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_organization_products_partial_update_error_type_20
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_organization_products_partial_update_error_type_21 = (
                        ApiV1PricingOrganizationProductsPartialUpdateSlaAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_organization_products_partial_update_error_type_21
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_organization_products_partial_update_error_type_22 = (
                        ApiV1PricingOrganizationProductsPartialUpdateCatalogueAppErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_organization_products_partial_update_error_type_22
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_organization_products_partial_update_error_type_23 = (
                        ApiV1PricingOrganizationProductsPartialUpdateContentTypeErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_organization_products_partial_update_error_type_23
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_organization_products_partial_update_error_type_24 = (
                        ApiV1PricingOrganizationProductsPartialUpdateObjectIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_organization_products_partial_update_error_type_24
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_organization_products_partial_update_error_type_25 = (
                        ApiV1PricingOrganizationProductsPartialUpdateAutoManagedErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_organization_products_partial_update_error_type_25
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_organization_products_partial_update_error_type_26 = (
                        ApiV1PricingOrganizationProductsPartialUpdateActiveFromErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_organization_products_partial_update_error_type_26
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_organization_products_partial_update_error_type_27 = (
                        ApiV1PricingOrganizationProductsPartialUpdateActiveUntilErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_organization_products_partial_update_error_type_27
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_organization_products_partial_update_error_type_28 = (
                        ApiV1PricingOrganizationProductsPartialUpdateAgreedPriceErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_organization_products_partial_update_error_type_28
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_organization_products_partial_update_error_type_29 = (
                        ApiV1PricingOrganizationProductsPartialUpdateAgreedPriceReasonErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_organization_products_partial_update_error_type_29
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_api_v1_pricing_organization_products_partial_update_error_type_30 = (
                    ApiV1PricingOrganizationProductsPartialUpdateInternalNoteErrorComponent.from_dict(data)
                )

                return componentsschemas_api_v1_pricing_organization_products_partial_update_error_type_30

            errors_item = _parse_errors_item(errors_item_data)

            errors.append(errors_item)

        api_v1_pricing_organization_products_partial_update_validation_error = cls(
            type_=type_,
            errors=errors,
        )

        api_v1_pricing_organization_products_partial_update_validation_error.additional_properties = d
        return api_v1_pricing_organization_products_partial_update_validation_error

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
