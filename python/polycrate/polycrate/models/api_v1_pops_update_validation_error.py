from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.validation_error_enum import ValidationErrorEnum, check_validation_error_enum

if TYPE_CHECKING:
    from ..models.api_v1_pops_update_annotations_error_component import ApiV1PopsUpdateAnnotationsErrorComponent
    from ..models.api_v1_pops_update_archived_at_error_component import ApiV1PopsUpdateArchivedAtErrorComponent
    from ..models.api_v1_pops_update_archived_error_component import ApiV1PopsUpdateArchivedErrorComponent
    from ..models.api_v1_pops_update_archived_reason_error_component import ApiV1PopsUpdateArchivedReasonErrorComponent
    from ..models.api_v1_pops_update_city_error_component import ApiV1PopsUpdateCityErrorComponent
    from ..models.api_v1_pops_update_country_error_component import ApiV1PopsUpdateCountryErrorComponent
    from ..models.api_v1_pops_update_criticality_error_component import ApiV1PopsUpdateCriticalityErrorComponent
    from ..models.api_v1_pops_update_debug_mode_error_component import ApiV1PopsUpdateDebugModeErrorComponent
    from ..models.api_v1_pops_update_description_error_component import ApiV1PopsUpdateDescriptionErrorComponent
    from ..models.api_v1_pops_update_display_name_error_component import ApiV1PopsUpdateDisplayNameErrorComponent
    from ..models.api_v1_pops_update_kind_error_component import ApiV1PopsUpdateKindErrorComponent
    from ..models.api_v1_pops_update_labels_error_component import ApiV1PopsUpdateLabelsErrorComponent
    from ..models.api_v1_pops_update_latitude_error_component import ApiV1PopsUpdateLatitudeErrorComponent
    from ..models.api_v1_pops_update_longitude_error_component import ApiV1PopsUpdateLongitudeErrorComponent
    from ..models.api_v1_pops_update_name_error_component import ApiV1PopsUpdateNameErrorComponent
    from ..models.api_v1_pops_update_non_field_errors_error_component import ApiV1PopsUpdateNonFieldErrorsErrorComponent
    from ..models.api_v1_pops_update_platform_service_error_component import (
        ApiV1PopsUpdatePlatformServiceErrorComponent,
    )
    from ..models.api_v1_pops_update_pop_endpoint_remote_address_error_component import (
        ApiV1PopsUpdatePopEndpointRemoteAddressErrorComponent,
    )
    from ..models.api_v1_pops_update_provider_entity_id_error_component import (
        ApiV1PopsUpdateProviderEntityIdErrorComponent,
    )
    from ..models.api_v1_pops_update_provider_error_component import ApiV1PopsUpdateProviderErrorComponent
    from ..models.api_v1_pops_update_provider_id_error_component import ApiV1PopsUpdateProviderIdErrorComponent
    from ..models.api_v1_pops_update_provider_reference_error_component import (
        ApiV1PopsUpdateProviderReferenceErrorComponent,
    )
    from ..models.api_v1_pops_update_reconciliation_enabled_error_component import (
        ApiV1PopsUpdateReconciliationEnabledErrorComponent,
    )
    from ..models.api_v1_pops_update_region_error_component import ApiV1PopsUpdateRegionErrorComponent
    from ..models.api_v1_pops_update_sla_availability_error_component import (
        ApiV1PopsUpdateSlaAvailabilityErrorComponent,
    )
    from ..models.api_v1_pops_update_sla_target_error_component import ApiV1PopsUpdateSlaTargetErrorComponent
    from ..models.api_v1_pops_update_slo_availability_error_component import (
        ApiV1PopsUpdateSloAvailabilityErrorComponent,
    )
    from ..models.api_v1_pops_update_slo_target_error_component import ApiV1PopsUpdateSloTargetErrorComponent
    from ..models.api_v1_pops_update_target_availability_error_component import (
        ApiV1PopsUpdateTargetAvailabilityErrorComponent,
    )
    from ..models.api_v1_pops_update_tolerations_error_component import ApiV1PopsUpdateTolerationsErrorComponent


T = TypeVar("T", bound="ApiV1PopsUpdateValidationError")


@_attrs_define
class ApiV1PopsUpdateValidationError:
    """
    Attributes:
        type_ (ValidationErrorEnum): * `validation_error` - Validation Error
        errors (list[ApiV1PopsUpdateAnnotationsErrorComponent | ApiV1PopsUpdateArchivedAtErrorComponent |
            ApiV1PopsUpdateArchivedErrorComponent | ApiV1PopsUpdateArchivedReasonErrorComponent |
            ApiV1PopsUpdateCityErrorComponent | ApiV1PopsUpdateCountryErrorComponent |
            ApiV1PopsUpdateCriticalityErrorComponent | ApiV1PopsUpdateDebugModeErrorComponent |
            ApiV1PopsUpdateDescriptionErrorComponent | ApiV1PopsUpdateDisplayNameErrorComponent |
            ApiV1PopsUpdateKindErrorComponent | ApiV1PopsUpdateLabelsErrorComponent | ApiV1PopsUpdateLatitudeErrorComponent
            | ApiV1PopsUpdateLongitudeErrorComponent | ApiV1PopsUpdateNameErrorComponent |
            ApiV1PopsUpdateNonFieldErrorsErrorComponent | ApiV1PopsUpdatePlatformServiceErrorComponent |
            ApiV1PopsUpdatePopEndpointRemoteAddressErrorComponent | ApiV1PopsUpdateProviderEntityIdErrorComponent |
            ApiV1PopsUpdateProviderErrorComponent | ApiV1PopsUpdateProviderIdErrorComponent |
            ApiV1PopsUpdateProviderReferenceErrorComponent | ApiV1PopsUpdateReconciliationEnabledErrorComponent |
            ApiV1PopsUpdateRegionErrorComponent | ApiV1PopsUpdateSlaAvailabilityErrorComponent |
            ApiV1PopsUpdateSlaTargetErrorComponent | ApiV1PopsUpdateSloAvailabilityErrorComponent |
            ApiV1PopsUpdateSloTargetErrorComponent | ApiV1PopsUpdateTargetAvailabilityErrorComponent |
            ApiV1PopsUpdateTolerationsErrorComponent]):
    """

    type_: ValidationErrorEnum
    errors: list[
        ApiV1PopsUpdateAnnotationsErrorComponent
        | ApiV1PopsUpdateArchivedAtErrorComponent
        | ApiV1PopsUpdateArchivedErrorComponent
        | ApiV1PopsUpdateArchivedReasonErrorComponent
        | ApiV1PopsUpdateCityErrorComponent
        | ApiV1PopsUpdateCountryErrorComponent
        | ApiV1PopsUpdateCriticalityErrorComponent
        | ApiV1PopsUpdateDebugModeErrorComponent
        | ApiV1PopsUpdateDescriptionErrorComponent
        | ApiV1PopsUpdateDisplayNameErrorComponent
        | ApiV1PopsUpdateKindErrorComponent
        | ApiV1PopsUpdateLabelsErrorComponent
        | ApiV1PopsUpdateLatitudeErrorComponent
        | ApiV1PopsUpdateLongitudeErrorComponent
        | ApiV1PopsUpdateNameErrorComponent
        | ApiV1PopsUpdateNonFieldErrorsErrorComponent
        | ApiV1PopsUpdatePlatformServiceErrorComponent
        | ApiV1PopsUpdatePopEndpointRemoteAddressErrorComponent
        | ApiV1PopsUpdateProviderEntityIdErrorComponent
        | ApiV1PopsUpdateProviderErrorComponent
        | ApiV1PopsUpdateProviderIdErrorComponent
        | ApiV1PopsUpdateProviderReferenceErrorComponent
        | ApiV1PopsUpdateReconciliationEnabledErrorComponent
        | ApiV1PopsUpdateRegionErrorComponent
        | ApiV1PopsUpdateSlaAvailabilityErrorComponent
        | ApiV1PopsUpdateSlaTargetErrorComponent
        | ApiV1PopsUpdateSloAvailabilityErrorComponent
        | ApiV1PopsUpdateSloTargetErrorComponent
        | ApiV1PopsUpdateTargetAvailabilityErrorComponent
        | ApiV1PopsUpdateTolerationsErrorComponent
    ]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.api_v1_pops_update_annotations_error_component import ApiV1PopsUpdateAnnotationsErrorComponent
        from ..models.api_v1_pops_update_archived_at_error_component import ApiV1PopsUpdateArchivedAtErrorComponent
        from ..models.api_v1_pops_update_archived_error_component import ApiV1PopsUpdateArchivedErrorComponent
        from ..models.api_v1_pops_update_archived_reason_error_component import (
            ApiV1PopsUpdateArchivedReasonErrorComponent,
        )
        from ..models.api_v1_pops_update_city_error_component import ApiV1PopsUpdateCityErrorComponent
        from ..models.api_v1_pops_update_country_error_component import ApiV1PopsUpdateCountryErrorComponent
        from ..models.api_v1_pops_update_criticality_error_component import ApiV1PopsUpdateCriticalityErrorComponent
        from ..models.api_v1_pops_update_debug_mode_error_component import ApiV1PopsUpdateDebugModeErrorComponent
        from ..models.api_v1_pops_update_description_error_component import ApiV1PopsUpdateDescriptionErrorComponent
        from ..models.api_v1_pops_update_display_name_error_component import ApiV1PopsUpdateDisplayNameErrorComponent
        from ..models.api_v1_pops_update_kind_error_component import ApiV1PopsUpdateKindErrorComponent
        from ..models.api_v1_pops_update_labels_error_component import ApiV1PopsUpdateLabelsErrorComponent
        from ..models.api_v1_pops_update_latitude_error_component import ApiV1PopsUpdateLatitudeErrorComponent
        from ..models.api_v1_pops_update_longitude_error_component import ApiV1PopsUpdateLongitudeErrorComponent
        from ..models.api_v1_pops_update_name_error_component import ApiV1PopsUpdateNameErrorComponent
        from ..models.api_v1_pops_update_non_field_errors_error_component import (
            ApiV1PopsUpdateNonFieldErrorsErrorComponent,
        )
        from ..models.api_v1_pops_update_platform_service_error_component import (
            ApiV1PopsUpdatePlatformServiceErrorComponent,
        )
        from ..models.api_v1_pops_update_provider_entity_id_error_component import (
            ApiV1PopsUpdateProviderEntityIdErrorComponent,
        )
        from ..models.api_v1_pops_update_provider_error_component import ApiV1PopsUpdateProviderErrorComponent
        from ..models.api_v1_pops_update_provider_id_error_component import ApiV1PopsUpdateProviderIdErrorComponent
        from ..models.api_v1_pops_update_provider_reference_error_component import (
            ApiV1PopsUpdateProviderReferenceErrorComponent,
        )
        from ..models.api_v1_pops_update_reconciliation_enabled_error_component import (
            ApiV1PopsUpdateReconciliationEnabledErrorComponent,
        )
        from ..models.api_v1_pops_update_region_error_component import ApiV1PopsUpdateRegionErrorComponent
        from ..models.api_v1_pops_update_sla_availability_error_component import (
            ApiV1PopsUpdateSlaAvailabilityErrorComponent,
        )
        from ..models.api_v1_pops_update_sla_target_error_component import ApiV1PopsUpdateSlaTargetErrorComponent
        from ..models.api_v1_pops_update_slo_availability_error_component import (
            ApiV1PopsUpdateSloAvailabilityErrorComponent,
        )
        from ..models.api_v1_pops_update_slo_target_error_component import ApiV1PopsUpdateSloTargetErrorComponent
        from ..models.api_v1_pops_update_target_availability_error_component import (
            ApiV1PopsUpdateTargetAvailabilityErrorComponent,
        )
        from ..models.api_v1_pops_update_tolerations_error_component import ApiV1PopsUpdateTolerationsErrorComponent

        type_: str = self.type_

        errors = []
        for errors_item_data in self.errors:
            errors_item: dict[str, Any]
            if isinstance(errors_item_data, ApiV1PopsUpdateNonFieldErrorsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PopsUpdateNameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PopsUpdateDisplayNameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PopsUpdateLabelsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PopsUpdateAnnotationsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PopsUpdateDebugModeErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PopsUpdateProviderErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PopsUpdateProviderReferenceErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PopsUpdateProviderIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PopsUpdateReconciliationEnabledErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PopsUpdatePlatformServiceErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PopsUpdateKindErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PopsUpdateTolerationsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PopsUpdateArchivedErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PopsUpdateArchivedAtErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PopsUpdateArchivedReasonErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PopsUpdateCriticalityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PopsUpdateTargetAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PopsUpdateSloTargetErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PopsUpdateSloAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PopsUpdateSlaTargetErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PopsUpdateSlaAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PopsUpdateRegionErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PopsUpdateCountryErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PopsUpdateCityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PopsUpdateDescriptionErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PopsUpdateLatitudeErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PopsUpdateLongitudeErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PopsUpdateProviderEntityIdErrorComponent):
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
        from ..models.api_v1_pops_update_annotations_error_component import ApiV1PopsUpdateAnnotationsErrorComponent
        from ..models.api_v1_pops_update_archived_at_error_component import ApiV1PopsUpdateArchivedAtErrorComponent
        from ..models.api_v1_pops_update_archived_error_component import ApiV1PopsUpdateArchivedErrorComponent
        from ..models.api_v1_pops_update_archived_reason_error_component import (
            ApiV1PopsUpdateArchivedReasonErrorComponent,
        )
        from ..models.api_v1_pops_update_city_error_component import ApiV1PopsUpdateCityErrorComponent
        from ..models.api_v1_pops_update_country_error_component import ApiV1PopsUpdateCountryErrorComponent
        from ..models.api_v1_pops_update_criticality_error_component import ApiV1PopsUpdateCriticalityErrorComponent
        from ..models.api_v1_pops_update_debug_mode_error_component import ApiV1PopsUpdateDebugModeErrorComponent
        from ..models.api_v1_pops_update_description_error_component import ApiV1PopsUpdateDescriptionErrorComponent
        from ..models.api_v1_pops_update_display_name_error_component import ApiV1PopsUpdateDisplayNameErrorComponent
        from ..models.api_v1_pops_update_kind_error_component import ApiV1PopsUpdateKindErrorComponent
        from ..models.api_v1_pops_update_labels_error_component import ApiV1PopsUpdateLabelsErrorComponent
        from ..models.api_v1_pops_update_latitude_error_component import ApiV1PopsUpdateLatitudeErrorComponent
        from ..models.api_v1_pops_update_longitude_error_component import ApiV1PopsUpdateLongitudeErrorComponent
        from ..models.api_v1_pops_update_name_error_component import ApiV1PopsUpdateNameErrorComponent
        from ..models.api_v1_pops_update_non_field_errors_error_component import (
            ApiV1PopsUpdateNonFieldErrorsErrorComponent,
        )
        from ..models.api_v1_pops_update_platform_service_error_component import (
            ApiV1PopsUpdatePlatformServiceErrorComponent,
        )
        from ..models.api_v1_pops_update_pop_endpoint_remote_address_error_component import (
            ApiV1PopsUpdatePopEndpointRemoteAddressErrorComponent,
        )
        from ..models.api_v1_pops_update_provider_entity_id_error_component import (
            ApiV1PopsUpdateProviderEntityIdErrorComponent,
        )
        from ..models.api_v1_pops_update_provider_error_component import ApiV1PopsUpdateProviderErrorComponent
        from ..models.api_v1_pops_update_provider_id_error_component import ApiV1PopsUpdateProviderIdErrorComponent
        from ..models.api_v1_pops_update_provider_reference_error_component import (
            ApiV1PopsUpdateProviderReferenceErrorComponent,
        )
        from ..models.api_v1_pops_update_reconciliation_enabled_error_component import (
            ApiV1PopsUpdateReconciliationEnabledErrorComponent,
        )
        from ..models.api_v1_pops_update_region_error_component import ApiV1PopsUpdateRegionErrorComponent
        from ..models.api_v1_pops_update_sla_availability_error_component import (
            ApiV1PopsUpdateSlaAvailabilityErrorComponent,
        )
        from ..models.api_v1_pops_update_sla_target_error_component import ApiV1PopsUpdateSlaTargetErrorComponent
        from ..models.api_v1_pops_update_slo_availability_error_component import (
            ApiV1PopsUpdateSloAvailabilityErrorComponent,
        )
        from ..models.api_v1_pops_update_slo_target_error_component import ApiV1PopsUpdateSloTargetErrorComponent
        from ..models.api_v1_pops_update_target_availability_error_component import (
            ApiV1PopsUpdateTargetAvailabilityErrorComponent,
        )
        from ..models.api_v1_pops_update_tolerations_error_component import ApiV1PopsUpdateTolerationsErrorComponent

        d = dict(src_dict)
        type_ = check_validation_error_enum(d.pop("type"))

        errors = []
        _errors = d.pop("errors")
        for errors_item_data in _errors:

            def _parse_errors_item(
                data: object,
            ) -> (
                ApiV1PopsUpdateAnnotationsErrorComponent
                | ApiV1PopsUpdateArchivedAtErrorComponent
                | ApiV1PopsUpdateArchivedErrorComponent
                | ApiV1PopsUpdateArchivedReasonErrorComponent
                | ApiV1PopsUpdateCityErrorComponent
                | ApiV1PopsUpdateCountryErrorComponent
                | ApiV1PopsUpdateCriticalityErrorComponent
                | ApiV1PopsUpdateDebugModeErrorComponent
                | ApiV1PopsUpdateDescriptionErrorComponent
                | ApiV1PopsUpdateDisplayNameErrorComponent
                | ApiV1PopsUpdateKindErrorComponent
                | ApiV1PopsUpdateLabelsErrorComponent
                | ApiV1PopsUpdateLatitudeErrorComponent
                | ApiV1PopsUpdateLongitudeErrorComponent
                | ApiV1PopsUpdateNameErrorComponent
                | ApiV1PopsUpdateNonFieldErrorsErrorComponent
                | ApiV1PopsUpdatePlatformServiceErrorComponent
                | ApiV1PopsUpdatePopEndpointRemoteAddressErrorComponent
                | ApiV1PopsUpdateProviderEntityIdErrorComponent
                | ApiV1PopsUpdateProviderErrorComponent
                | ApiV1PopsUpdateProviderIdErrorComponent
                | ApiV1PopsUpdateProviderReferenceErrorComponent
                | ApiV1PopsUpdateReconciliationEnabledErrorComponent
                | ApiV1PopsUpdateRegionErrorComponent
                | ApiV1PopsUpdateSlaAvailabilityErrorComponent
                | ApiV1PopsUpdateSlaTargetErrorComponent
                | ApiV1PopsUpdateSloAvailabilityErrorComponent
                | ApiV1PopsUpdateSloTargetErrorComponent
                | ApiV1PopsUpdateTargetAvailabilityErrorComponent
                | ApiV1PopsUpdateTolerationsErrorComponent
            ):
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pops_update_error_type_0 = (
                        ApiV1PopsUpdateNonFieldErrorsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pops_update_error_type_0
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pops_update_error_type_1 = ApiV1PopsUpdateNameErrorComponent.from_dict(
                        data
                    )

                    return componentsschemas_api_v1_pops_update_error_type_1
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pops_update_error_type_2 = (
                        ApiV1PopsUpdateDisplayNameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pops_update_error_type_2
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pops_update_error_type_3 = ApiV1PopsUpdateLabelsErrorComponent.from_dict(
                        data
                    )

                    return componentsschemas_api_v1_pops_update_error_type_3
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pops_update_error_type_4 = (
                        ApiV1PopsUpdateAnnotationsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pops_update_error_type_4
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pops_update_error_type_5 = (
                        ApiV1PopsUpdateDebugModeErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pops_update_error_type_5
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pops_update_error_type_6 = ApiV1PopsUpdateProviderErrorComponent.from_dict(
                        data
                    )

                    return componentsschemas_api_v1_pops_update_error_type_6
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pops_update_error_type_7 = (
                        ApiV1PopsUpdateProviderReferenceErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pops_update_error_type_7
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pops_update_error_type_8 = (
                        ApiV1PopsUpdateProviderIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pops_update_error_type_8
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pops_update_error_type_9 = (
                        ApiV1PopsUpdateReconciliationEnabledErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pops_update_error_type_9
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pops_update_error_type_10 = (
                        ApiV1PopsUpdatePlatformServiceErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pops_update_error_type_10
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pops_update_error_type_11 = ApiV1PopsUpdateKindErrorComponent.from_dict(
                        data
                    )

                    return componentsschemas_api_v1_pops_update_error_type_11
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pops_update_error_type_12 = (
                        ApiV1PopsUpdateTolerationsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pops_update_error_type_12
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pops_update_error_type_13 = (
                        ApiV1PopsUpdateArchivedErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pops_update_error_type_13
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pops_update_error_type_14 = (
                        ApiV1PopsUpdateArchivedAtErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pops_update_error_type_14
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pops_update_error_type_15 = (
                        ApiV1PopsUpdateArchivedReasonErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pops_update_error_type_15
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pops_update_error_type_16 = (
                        ApiV1PopsUpdateCriticalityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pops_update_error_type_16
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pops_update_error_type_17 = (
                        ApiV1PopsUpdateTargetAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pops_update_error_type_17
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pops_update_error_type_18 = (
                        ApiV1PopsUpdateSloTargetErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pops_update_error_type_18
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pops_update_error_type_19 = (
                        ApiV1PopsUpdateSloAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pops_update_error_type_19
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pops_update_error_type_20 = (
                        ApiV1PopsUpdateSlaTargetErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pops_update_error_type_20
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pops_update_error_type_21 = (
                        ApiV1PopsUpdateSlaAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pops_update_error_type_21
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pops_update_error_type_22 = ApiV1PopsUpdateRegionErrorComponent.from_dict(
                        data
                    )

                    return componentsschemas_api_v1_pops_update_error_type_22
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pops_update_error_type_23 = ApiV1PopsUpdateCountryErrorComponent.from_dict(
                        data
                    )

                    return componentsschemas_api_v1_pops_update_error_type_23
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pops_update_error_type_24 = ApiV1PopsUpdateCityErrorComponent.from_dict(
                        data
                    )

                    return componentsschemas_api_v1_pops_update_error_type_24
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pops_update_error_type_25 = (
                        ApiV1PopsUpdateDescriptionErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pops_update_error_type_25
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pops_update_error_type_26 = (
                        ApiV1PopsUpdateLatitudeErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pops_update_error_type_26
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pops_update_error_type_27 = (
                        ApiV1PopsUpdateLongitudeErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pops_update_error_type_27
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pops_update_error_type_28 = (
                        ApiV1PopsUpdateProviderEntityIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pops_update_error_type_28
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_api_v1_pops_update_error_type_29 = (
                    ApiV1PopsUpdatePopEndpointRemoteAddressErrorComponent.from_dict(data)
                )

                return componentsschemas_api_v1_pops_update_error_type_29

            errors_item = _parse_errors_item(errors_item_data)

            errors.append(errors_item)

        api_v1_pops_update_validation_error = cls(
            type_=type_,
            errors=errors,
        )

        api_v1_pops_update_validation_error.additional_properties = d
        return api_v1_pops_update_validation_error

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
