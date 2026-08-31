from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.validation_error_enum import ValidationErrorEnum, check_validation_error_enum

if TYPE_CHECKING:
    from ..models.api_v1_pops_partial_update_annotations_error_component import (
        ApiV1PopsPartialUpdateAnnotationsErrorComponent,
    )
    from ..models.api_v1_pops_partial_update_archived_at_error_component import (
        ApiV1PopsPartialUpdateArchivedAtErrorComponent,
    )
    from ..models.api_v1_pops_partial_update_archived_error_component import (
        ApiV1PopsPartialUpdateArchivedErrorComponent,
    )
    from ..models.api_v1_pops_partial_update_archived_reason_error_component import (
        ApiV1PopsPartialUpdateArchivedReasonErrorComponent,
    )
    from ..models.api_v1_pops_partial_update_city_error_component import ApiV1PopsPartialUpdateCityErrorComponent
    from ..models.api_v1_pops_partial_update_country_error_component import ApiV1PopsPartialUpdateCountryErrorComponent
    from ..models.api_v1_pops_partial_update_criticality_error_component import (
        ApiV1PopsPartialUpdateCriticalityErrorComponent,
    )
    from ..models.api_v1_pops_partial_update_debug_mode_error_component import (
        ApiV1PopsPartialUpdateDebugModeErrorComponent,
    )
    from ..models.api_v1_pops_partial_update_description_error_component import (
        ApiV1PopsPartialUpdateDescriptionErrorComponent,
    )
    from ..models.api_v1_pops_partial_update_display_name_error_component import (
        ApiV1PopsPartialUpdateDisplayNameErrorComponent,
    )
    from ..models.api_v1_pops_partial_update_kind_error_component import ApiV1PopsPartialUpdateKindErrorComponent
    from ..models.api_v1_pops_partial_update_labels_error_component import ApiV1PopsPartialUpdateLabelsErrorComponent
    from ..models.api_v1_pops_partial_update_latitude_error_component import (
        ApiV1PopsPartialUpdateLatitudeErrorComponent,
    )
    from ..models.api_v1_pops_partial_update_longitude_error_component import (
        ApiV1PopsPartialUpdateLongitudeErrorComponent,
    )
    from ..models.api_v1_pops_partial_update_name_error_component import ApiV1PopsPartialUpdateNameErrorComponent
    from ..models.api_v1_pops_partial_update_non_field_errors_error_component import (
        ApiV1PopsPartialUpdateNonFieldErrorsErrorComponent,
    )
    from ..models.api_v1_pops_partial_update_platform_service_error_component import (
        ApiV1PopsPartialUpdatePlatformServiceErrorComponent,
    )
    from ..models.api_v1_pops_partial_update_pop_endpoint_remote_address_error_component import (
        ApiV1PopsPartialUpdatePopEndpointRemoteAddressErrorComponent,
    )
    from ..models.api_v1_pops_partial_update_provider_entity_id_error_component import (
        ApiV1PopsPartialUpdateProviderEntityIdErrorComponent,
    )
    from ..models.api_v1_pops_partial_update_provider_error_component import (
        ApiV1PopsPartialUpdateProviderErrorComponent,
    )
    from ..models.api_v1_pops_partial_update_provider_id_error_component import (
        ApiV1PopsPartialUpdateProviderIdErrorComponent,
    )
    from ..models.api_v1_pops_partial_update_provider_reference_error_component import (
        ApiV1PopsPartialUpdateProviderReferenceErrorComponent,
    )
    from ..models.api_v1_pops_partial_update_reconciliation_enabled_error_component import (
        ApiV1PopsPartialUpdateReconciliationEnabledErrorComponent,
    )
    from ..models.api_v1_pops_partial_update_region_error_component import ApiV1PopsPartialUpdateRegionErrorComponent
    from ..models.api_v1_pops_partial_update_sla_availability_error_component import (
        ApiV1PopsPartialUpdateSlaAvailabilityErrorComponent,
    )
    from ..models.api_v1_pops_partial_update_sla_target_error_component import (
        ApiV1PopsPartialUpdateSlaTargetErrorComponent,
    )
    from ..models.api_v1_pops_partial_update_slo_availability_error_component import (
        ApiV1PopsPartialUpdateSloAvailabilityErrorComponent,
    )
    from ..models.api_v1_pops_partial_update_slo_target_error_component import (
        ApiV1PopsPartialUpdateSloTargetErrorComponent,
    )
    from ..models.api_v1_pops_partial_update_target_availability_error_component import (
        ApiV1PopsPartialUpdateTargetAvailabilityErrorComponent,
    )
    from ..models.api_v1_pops_partial_update_tolerations_error_component import (
        ApiV1PopsPartialUpdateTolerationsErrorComponent,
    )


T = TypeVar("T", bound="ApiV1PopsPartialUpdateValidationError")


@_attrs_define
class ApiV1PopsPartialUpdateValidationError:
    """
    Attributes:
        type_ (ValidationErrorEnum): * `validation_error` - Validation Error
        errors (list[ApiV1PopsPartialUpdateAnnotationsErrorComponent | ApiV1PopsPartialUpdateArchivedAtErrorComponent |
            ApiV1PopsPartialUpdateArchivedErrorComponent | ApiV1PopsPartialUpdateArchivedReasonErrorComponent |
            ApiV1PopsPartialUpdateCityErrorComponent | ApiV1PopsPartialUpdateCountryErrorComponent |
            ApiV1PopsPartialUpdateCriticalityErrorComponent | ApiV1PopsPartialUpdateDebugModeErrorComponent |
            ApiV1PopsPartialUpdateDescriptionErrorComponent | ApiV1PopsPartialUpdateDisplayNameErrorComponent |
            ApiV1PopsPartialUpdateKindErrorComponent | ApiV1PopsPartialUpdateLabelsErrorComponent |
            ApiV1PopsPartialUpdateLatitudeErrorComponent | ApiV1PopsPartialUpdateLongitudeErrorComponent |
            ApiV1PopsPartialUpdateNameErrorComponent | ApiV1PopsPartialUpdateNonFieldErrorsErrorComponent |
            ApiV1PopsPartialUpdatePlatformServiceErrorComponent |
            ApiV1PopsPartialUpdatePopEndpointRemoteAddressErrorComponent |
            ApiV1PopsPartialUpdateProviderEntityIdErrorComponent | ApiV1PopsPartialUpdateProviderErrorComponent |
            ApiV1PopsPartialUpdateProviderIdErrorComponent | ApiV1PopsPartialUpdateProviderReferenceErrorComponent |
            ApiV1PopsPartialUpdateReconciliationEnabledErrorComponent | ApiV1PopsPartialUpdateRegionErrorComponent |
            ApiV1PopsPartialUpdateSlaAvailabilityErrorComponent | ApiV1PopsPartialUpdateSlaTargetErrorComponent |
            ApiV1PopsPartialUpdateSloAvailabilityErrorComponent | ApiV1PopsPartialUpdateSloTargetErrorComponent |
            ApiV1PopsPartialUpdateTargetAvailabilityErrorComponent | ApiV1PopsPartialUpdateTolerationsErrorComponent]):
    """

    type_: ValidationErrorEnum
    errors: list[
        ApiV1PopsPartialUpdateAnnotationsErrorComponent
        | ApiV1PopsPartialUpdateArchivedAtErrorComponent
        | ApiV1PopsPartialUpdateArchivedErrorComponent
        | ApiV1PopsPartialUpdateArchivedReasonErrorComponent
        | ApiV1PopsPartialUpdateCityErrorComponent
        | ApiV1PopsPartialUpdateCountryErrorComponent
        | ApiV1PopsPartialUpdateCriticalityErrorComponent
        | ApiV1PopsPartialUpdateDebugModeErrorComponent
        | ApiV1PopsPartialUpdateDescriptionErrorComponent
        | ApiV1PopsPartialUpdateDisplayNameErrorComponent
        | ApiV1PopsPartialUpdateKindErrorComponent
        | ApiV1PopsPartialUpdateLabelsErrorComponent
        | ApiV1PopsPartialUpdateLatitudeErrorComponent
        | ApiV1PopsPartialUpdateLongitudeErrorComponent
        | ApiV1PopsPartialUpdateNameErrorComponent
        | ApiV1PopsPartialUpdateNonFieldErrorsErrorComponent
        | ApiV1PopsPartialUpdatePlatformServiceErrorComponent
        | ApiV1PopsPartialUpdatePopEndpointRemoteAddressErrorComponent
        | ApiV1PopsPartialUpdateProviderEntityIdErrorComponent
        | ApiV1PopsPartialUpdateProviderErrorComponent
        | ApiV1PopsPartialUpdateProviderIdErrorComponent
        | ApiV1PopsPartialUpdateProviderReferenceErrorComponent
        | ApiV1PopsPartialUpdateReconciliationEnabledErrorComponent
        | ApiV1PopsPartialUpdateRegionErrorComponent
        | ApiV1PopsPartialUpdateSlaAvailabilityErrorComponent
        | ApiV1PopsPartialUpdateSlaTargetErrorComponent
        | ApiV1PopsPartialUpdateSloAvailabilityErrorComponent
        | ApiV1PopsPartialUpdateSloTargetErrorComponent
        | ApiV1PopsPartialUpdateTargetAvailabilityErrorComponent
        | ApiV1PopsPartialUpdateTolerationsErrorComponent
    ]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.api_v1_pops_partial_update_annotations_error_component import (
            ApiV1PopsPartialUpdateAnnotationsErrorComponent,
        )
        from ..models.api_v1_pops_partial_update_archived_at_error_component import (
            ApiV1PopsPartialUpdateArchivedAtErrorComponent,
        )
        from ..models.api_v1_pops_partial_update_archived_error_component import (
            ApiV1PopsPartialUpdateArchivedErrorComponent,
        )
        from ..models.api_v1_pops_partial_update_archived_reason_error_component import (
            ApiV1PopsPartialUpdateArchivedReasonErrorComponent,
        )
        from ..models.api_v1_pops_partial_update_city_error_component import ApiV1PopsPartialUpdateCityErrorComponent
        from ..models.api_v1_pops_partial_update_country_error_component import (
            ApiV1PopsPartialUpdateCountryErrorComponent,
        )
        from ..models.api_v1_pops_partial_update_criticality_error_component import (
            ApiV1PopsPartialUpdateCriticalityErrorComponent,
        )
        from ..models.api_v1_pops_partial_update_debug_mode_error_component import (
            ApiV1PopsPartialUpdateDebugModeErrorComponent,
        )
        from ..models.api_v1_pops_partial_update_description_error_component import (
            ApiV1PopsPartialUpdateDescriptionErrorComponent,
        )
        from ..models.api_v1_pops_partial_update_display_name_error_component import (
            ApiV1PopsPartialUpdateDisplayNameErrorComponent,
        )
        from ..models.api_v1_pops_partial_update_kind_error_component import ApiV1PopsPartialUpdateKindErrorComponent
        from ..models.api_v1_pops_partial_update_labels_error_component import (
            ApiV1PopsPartialUpdateLabelsErrorComponent,
        )
        from ..models.api_v1_pops_partial_update_latitude_error_component import (
            ApiV1PopsPartialUpdateLatitudeErrorComponent,
        )
        from ..models.api_v1_pops_partial_update_longitude_error_component import (
            ApiV1PopsPartialUpdateLongitudeErrorComponent,
        )
        from ..models.api_v1_pops_partial_update_name_error_component import ApiV1PopsPartialUpdateNameErrorComponent
        from ..models.api_v1_pops_partial_update_non_field_errors_error_component import (
            ApiV1PopsPartialUpdateNonFieldErrorsErrorComponent,
        )
        from ..models.api_v1_pops_partial_update_platform_service_error_component import (
            ApiV1PopsPartialUpdatePlatformServiceErrorComponent,
        )
        from ..models.api_v1_pops_partial_update_provider_entity_id_error_component import (
            ApiV1PopsPartialUpdateProviderEntityIdErrorComponent,
        )
        from ..models.api_v1_pops_partial_update_provider_error_component import (
            ApiV1PopsPartialUpdateProviderErrorComponent,
        )
        from ..models.api_v1_pops_partial_update_provider_id_error_component import (
            ApiV1PopsPartialUpdateProviderIdErrorComponent,
        )
        from ..models.api_v1_pops_partial_update_provider_reference_error_component import (
            ApiV1PopsPartialUpdateProviderReferenceErrorComponent,
        )
        from ..models.api_v1_pops_partial_update_reconciliation_enabled_error_component import (
            ApiV1PopsPartialUpdateReconciliationEnabledErrorComponent,
        )
        from ..models.api_v1_pops_partial_update_region_error_component import (
            ApiV1PopsPartialUpdateRegionErrorComponent,
        )
        from ..models.api_v1_pops_partial_update_sla_availability_error_component import (
            ApiV1PopsPartialUpdateSlaAvailabilityErrorComponent,
        )
        from ..models.api_v1_pops_partial_update_sla_target_error_component import (
            ApiV1PopsPartialUpdateSlaTargetErrorComponent,
        )
        from ..models.api_v1_pops_partial_update_slo_availability_error_component import (
            ApiV1PopsPartialUpdateSloAvailabilityErrorComponent,
        )
        from ..models.api_v1_pops_partial_update_slo_target_error_component import (
            ApiV1PopsPartialUpdateSloTargetErrorComponent,
        )
        from ..models.api_v1_pops_partial_update_target_availability_error_component import (
            ApiV1PopsPartialUpdateTargetAvailabilityErrorComponent,
        )
        from ..models.api_v1_pops_partial_update_tolerations_error_component import (
            ApiV1PopsPartialUpdateTolerationsErrorComponent,
        )

        type_: str = self.type_

        errors = []
        for errors_item_data in self.errors:
            errors_item: dict[str, Any]
            if isinstance(errors_item_data, ApiV1PopsPartialUpdateNonFieldErrorsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PopsPartialUpdateNameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PopsPartialUpdateDisplayNameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PopsPartialUpdateLabelsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PopsPartialUpdateAnnotationsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PopsPartialUpdateDebugModeErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PopsPartialUpdateProviderErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PopsPartialUpdateProviderReferenceErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PopsPartialUpdateProviderIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PopsPartialUpdateReconciliationEnabledErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PopsPartialUpdatePlatformServiceErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PopsPartialUpdateKindErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PopsPartialUpdateTolerationsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PopsPartialUpdateArchivedErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PopsPartialUpdateArchivedAtErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PopsPartialUpdateArchivedReasonErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PopsPartialUpdateCriticalityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PopsPartialUpdateTargetAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PopsPartialUpdateSloTargetErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PopsPartialUpdateSloAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PopsPartialUpdateSlaTargetErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PopsPartialUpdateSlaAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PopsPartialUpdateRegionErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PopsPartialUpdateCountryErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PopsPartialUpdateCityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PopsPartialUpdateDescriptionErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PopsPartialUpdateLatitudeErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PopsPartialUpdateLongitudeErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PopsPartialUpdateProviderEntityIdErrorComponent):
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
        from ..models.api_v1_pops_partial_update_annotations_error_component import (
            ApiV1PopsPartialUpdateAnnotationsErrorComponent,
        )
        from ..models.api_v1_pops_partial_update_archived_at_error_component import (
            ApiV1PopsPartialUpdateArchivedAtErrorComponent,
        )
        from ..models.api_v1_pops_partial_update_archived_error_component import (
            ApiV1PopsPartialUpdateArchivedErrorComponent,
        )
        from ..models.api_v1_pops_partial_update_archived_reason_error_component import (
            ApiV1PopsPartialUpdateArchivedReasonErrorComponent,
        )
        from ..models.api_v1_pops_partial_update_city_error_component import ApiV1PopsPartialUpdateCityErrorComponent
        from ..models.api_v1_pops_partial_update_country_error_component import (
            ApiV1PopsPartialUpdateCountryErrorComponent,
        )
        from ..models.api_v1_pops_partial_update_criticality_error_component import (
            ApiV1PopsPartialUpdateCriticalityErrorComponent,
        )
        from ..models.api_v1_pops_partial_update_debug_mode_error_component import (
            ApiV1PopsPartialUpdateDebugModeErrorComponent,
        )
        from ..models.api_v1_pops_partial_update_description_error_component import (
            ApiV1PopsPartialUpdateDescriptionErrorComponent,
        )
        from ..models.api_v1_pops_partial_update_display_name_error_component import (
            ApiV1PopsPartialUpdateDisplayNameErrorComponent,
        )
        from ..models.api_v1_pops_partial_update_kind_error_component import ApiV1PopsPartialUpdateKindErrorComponent
        from ..models.api_v1_pops_partial_update_labels_error_component import (
            ApiV1PopsPartialUpdateLabelsErrorComponent,
        )
        from ..models.api_v1_pops_partial_update_latitude_error_component import (
            ApiV1PopsPartialUpdateLatitudeErrorComponent,
        )
        from ..models.api_v1_pops_partial_update_longitude_error_component import (
            ApiV1PopsPartialUpdateLongitudeErrorComponent,
        )
        from ..models.api_v1_pops_partial_update_name_error_component import ApiV1PopsPartialUpdateNameErrorComponent
        from ..models.api_v1_pops_partial_update_non_field_errors_error_component import (
            ApiV1PopsPartialUpdateNonFieldErrorsErrorComponent,
        )
        from ..models.api_v1_pops_partial_update_platform_service_error_component import (
            ApiV1PopsPartialUpdatePlatformServiceErrorComponent,
        )
        from ..models.api_v1_pops_partial_update_pop_endpoint_remote_address_error_component import (
            ApiV1PopsPartialUpdatePopEndpointRemoteAddressErrorComponent,
        )
        from ..models.api_v1_pops_partial_update_provider_entity_id_error_component import (
            ApiV1PopsPartialUpdateProviderEntityIdErrorComponent,
        )
        from ..models.api_v1_pops_partial_update_provider_error_component import (
            ApiV1PopsPartialUpdateProviderErrorComponent,
        )
        from ..models.api_v1_pops_partial_update_provider_id_error_component import (
            ApiV1PopsPartialUpdateProviderIdErrorComponent,
        )
        from ..models.api_v1_pops_partial_update_provider_reference_error_component import (
            ApiV1PopsPartialUpdateProviderReferenceErrorComponent,
        )
        from ..models.api_v1_pops_partial_update_reconciliation_enabled_error_component import (
            ApiV1PopsPartialUpdateReconciliationEnabledErrorComponent,
        )
        from ..models.api_v1_pops_partial_update_region_error_component import (
            ApiV1PopsPartialUpdateRegionErrorComponent,
        )
        from ..models.api_v1_pops_partial_update_sla_availability_error_component import (
            ApiV1PopsPartialUpdateSlaAvailabilityErrorComponent,
        )
        from ..models.api_v1_pops_partial_update_sla_target_error_component import (
            ApiV1PopsPartialUpdateSlaTargetErrorComponent,
        )
        from ..models.api_v1_pops_partial_update_slo_availability_error_component import (
            ApiV1PopsPartialUpdateSloAvailabilityErrorComponent,
        )
        from ..models.api_v1_pops_partial_update_slo_target_error_component import (
            ApiV1PopsPartialUpdateSloTargetErrorComponent,
        )
        from ..models.api_v1_pops_partial_update_target_availability_error_component import (
            ApiV1PopsPartialUpdateTargetAvailabilityErrorComponent,
        )
        from ..models.api_v1_pops_partial_update_tolerations_error_component import (
            ApiV1PopsPartialUpdateTolerationsErrorComponent,
        )

        d = dict(src_dict)
        type_ = check_validation_error_enum(d.pop("type"))

        errors = []
        _errors = d.pop("errors")
        for errors_item_data in _errors:

            def _parse_errors_item(
                data: object,
            ) -> (
                ApiV1PopsPartialUpdateAnnotationsErrorComponent
                | ApiV1PopsPartialUpdateArchivedAtErrorComponent
                | ApiV1PopsPartialUpdateArchivedErrorComponent
                | ApiV1PopsPartialUpdateArchivedReasonErrorComponent
                | ApiV1PopsPartialUpdateCityErrorComponent
                | ApiV1PopsPartialUpdateCountryErrorComponent
                | ApiV1PopsPartialUpdateCriticalityErrorComponent
                | ApiV1PopsPartialUpdateDebugModeErrorComponent
                | ApiV1PopsPartialUpdateDescriptionErrorComponent
                | ApiV1PopsPartialUpdateDisplayNameErrorComponent
                | ApiV1PopsPartialUpdateKindErrorComponent
                | ApiV1PopsPartialUpdateLabelsErrorComponent
                | ApiV1PopsPartialUpdateLatitudeErrorComponent
                | ApiV1PopsPartialUpdateLongitudeErrorComponent
                | ApiV1PopsPartialUpdateNameErrorComponent
                | ApiV1PopsPartialUpdateNonFieldErrorsErrorComponent
                | ApiV1PopsPartialUpdatePlatformServiceErrorComponent
                | ApiV1PopsPartialUpdatePopEndpointRemoteAddressErrorComponent
                | ApiV1PopsPartialUpdateProviderEntityIdErrorComponent
                | ApiV1PopsPartialUpdateProviderErrorComponent
                | ApiV1PopsPartialUpdateProviderIdErrorComponent
                | ApiV1PopsPartialUpdateProviderReferenceErrorComponent
                | ApiV1PopsPartialUpdateReconciliationEnabledErrorComponent
                | ApiV1PopsPartialUpdateRegionErrorComponent
                | ApiV1PopsPartialUpdateSlaAvailabilityErrorComponent
                | ApiV1PopsPartialUpdateSlaTargetErrorComponent
                | ApiV1PopsPartialUpdateSloAvailabilityErrorComponent
                | ApiV1PopsPartialUpdateSloTargetErrorComponent
                | ApiV1PopsPartialUpdateTargetAvailabilityErrorComponent
                | ApiV1PopsPartialUpdateTolerationsErrorComponent
            ):
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pops_partial_update_error_type_0 = (
                        ApiV1PopsPartialUpdateNonFieldErrorsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pops_partial_update_error_type_0
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pops_partial_update_error_type_1 = (
                        ApiV1PopsPartialUpdateNameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pops_partial_update_error_type_1
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pops_partial_update_error_type_2 = (
                        ApiV1PopsPartialUpdateDisplayNameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pops_partial_update_error_type_2
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pops_partial_update_error_type_3 = (
                        ApiV1PopsPartialUpdateLabelsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pops_partial_update_error_type_3
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pops_partial_update_error_type_4 = (
                        ApiV1PopsPartialUpdateAnnotationsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pops_partial_update_error_type_4
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pops_partial_update_error_type_5 = (
                        ApiV1PopsPartialUpdateDebugModeErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pops_partial_update_error_type_5
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pops_partial_update_error_type_6 = (
                        ApiV1PopsPartialUpdateProviderErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pops_partial_update_error_type_6
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pops_partial_update_error_type_7 = (
                        ApiV1PopsPartialUpdateProviderReferenceErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pops_partial_update_error_type_7
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pops_partial_update_error_type_8 = (
                        ApiV1PopsPartialUpdateProviderIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pops_partial_update_error_type_8
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pops_partial_update_error_type_9 = (
                        ApiV1PopsPartialUpdateReconciliationEnabledErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pops_partial_update_error_type_9
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pops_partial_update_error_type_10 = (
                        ApiV1PopsPartialUpdatePlatformServiceErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pops_partial_update_error_type_10
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pops_partial_update_error_type_11 = (
                        ApiV1PopsPartialUpdateKindErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pops_partial_update_error_type_11
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pops_partial_update_error_type_12 = (
                        ApiV1PopsPartialUpdateTolerationsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pops_partial_update_error_type_12
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pops_partial_update_error_type_13 = (
                        ApiV1PopsPartialUpdateArchivedErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pops_partial_update_error_type_13
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pops_partial_update_error_type_14 = (
                        ApiV1PopsPartialUpdateArchivedAtErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pops_partial_update_error_type_14
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pops_partial_update_error_type_15 = (
                        ApiV1PopsPartialUpdateArchivedReasonErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pops_partial_update_error_type_15
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pops_partial_update_error_type_16 = (
                        ApiV1PopsPartialUpdateCriticalityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pops_partial_update_error_type_16
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pops_partial_update_error_type_17 = (
                        ApiV1PopsPartialUpdateTargetAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pops_partial_update_error_type_17
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pops_partial_update_error_type_18 = (
                        ApiV1PopsPartialUpdateSloTargetErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pops_partial_update_error_type_18
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pops_partial_update_error_type_19 = (
                        ApiV1PopsPartialUpdateSloAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pops_partial_update_error_type_19
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pops_partial_update_error_type_20 = (
                        ApiV1PopsPartialUpdateSlaTargetErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pops_partial_update_error_type_20
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pops_partial_update_error_type_21 = (
                        ApiV1PopsPartialUpdateSlaAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pops_partial_update_error_type_21
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pops_partial_update_error_type_22 = (
                        ApiV1PopsPartialUpdateRegionErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pops_partial_update_error_type_22
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pops_partial_update_error_type_23 = (
                        ApiV1PopsPartialUpdateCountryErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pops_partial_update_error_type_23
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pops_partial_update_error_type_24 = (
                        ApiV1PopsPartialUpdateCityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pops_partial_update_error_type_24
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pops_partial_update_error_type_25 = (
                        ApiV1PopsPartialUpdateDescriptionErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pops_partial_update_error_type_25
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pops_partial_update_error_type_26 = (
                        ApiV1PopsPartialUpdateLatitudeErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pops_partial_update_error_type_26
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pops_partial_update_error_type_27 = (
                        ApiV1PopsPartialUpdateLongitudeErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pops_partial_update_error_type_27
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pops_partial_update_error_type_28 = (
                        ApiV1PopsPartialUpdateProviderEntityIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pops_partial_update_error_type_28
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_api_v1_pops_partial_update_error_type_29 = (
                    ApiV1PopsPartialUpdatePopEndpointRemoteAddressErrorComponent.from_dict(data)
                )

                return componentsschemas_api_v1_pops_partial_update_error_type_29

            errors_item = _parse_errors_item(errors_item_data)

            errors.append(errors_item)

        api_v1_pops_partial_update_validation_error = cls(
            type_=type_,
            errors=errors,
        )

        api_v1_pops_partial_update_validation_error.additional_properties = d
        return api_v1_pops_partial_update_validation_error

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
